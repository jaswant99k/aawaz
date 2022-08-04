import os
import re

import firebase_admin
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone
from firebase_admin import auth
from firebase_admin import credentials
from rest_framework import authentication
from rest_framework import exceptions

from user_management.models import UserProfile


from .exceptions import FirebaseError
from .exceptions import InvalidAuthToken
from .exceptions import NoAuthToken
from django.contrib.auth import authenticate, login

cred = credentials.Certificate(
    {
        "type": "service_account",
        "project_id": "awaazproject-34fb8",
        "private_key_id": "d5122cf387b5b4a6714d6100700a66cbfa864f1c",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQDAXz54VrOBwtDN\nAKk8CaBc+9N8g/ZEk4uoFGz54I7ygg6ld2TkRoyyEFPad5SrEC3ig4xplC/lRwDX\nW/bYZE7magIEehTUCMlA0/rrNap12UGPm7iwQ667YopvHQUIY/yiCQOCG2k/SJHx\nFyQx+wuzhSzLTycpy+YGtAWFzecyOlu+u5xip4EablUUcgTbhCDaFJxHlCXh1wh7\nVW/aWIyWPK4kT3EIBvM6O+33dq/hVMvV4B8ziVVvsysbT1DhI7c3xjWmube7eGGC\npvvd2FzoerMCLfR51xmm1y/BCf6tL7xAv4I9rxTmIAv4+yemg2Jt/t/+BagoFm2G\neia4q7s3AgMBAAECggEARP8EJ2IlYOGQRS67BBsJxr/Vgv/LiJ4IxYCJ83dcndMS\n0LsJVyyMkuLzSFSCYHZdlrQK3OU25nt4bEWCO+uCNvcHgTaOGNyL3jIJeWoWmM0S\nzCCUdbfYyEGYGDEm2HMQLceg1/3f2kA7g+aCZ2C8uicGQWdCyyVj+7x+jJakmOkf\n3ed2tH9LiONsPeEG1KRkW6SjOSmdudmy/iO7uVM1ACnux0z7Sis/PJYIja89d+UR\nDnAPYtGfLtE1TOKOaEOTA5feUT4Ai11CCiE26T8/mynP4pAPJk4eLu0utVzkF886\nLPDndXmcSnWscNE7cdKzmtZXZMYAWD5k1+5pgWVUQQKBgQD9bRjKMkU6uS17Ebp2\n6enY7hCzNIcghUu23xLEkqcfzgUosbidutiaylBCCSgp50Gu/NY4IBHI+GG7IwHE\nnswiCTswcs5tWvMQsI7JpiFyrgDbqYsCz5SoQgYU2lpRiNX2qNTsPkd2aaWEec2z\nAZy7ZzbuHvl1dKWSr4HoHc/QQQKBgQDCU2hcr4l/rmaSR1xI+AJ3A7hAbEcWf7vs\nAQF7aGC+7IdG9ogYID58rzo4z1cZMKCs4dOV2g38rAbQ4hIDncc9iiCYAfxLN5P0\nUCwVMuS61j8Pw2nDej+xbWfoIynK/J3XWBJxYLXTL/a80GmC9x22iPI7eMxJuNRO\nQRhNl9atdwKBgQClFCWrwCc8Y1du7VNrFl/PgPO76CGFW47AZnrRNT5MB2Vw5qN9\nizKBUfwJp/FTqmIs3GGmWa18Hd97iQgjzdTm7uBxZLd2oGHoozm/vMnY6+N/Muds\nQ09wcuGHP9zJc7r8W2mnIcJnLdY1fyowyoIPyOINJnwUuJEKBe03CARQgQKBgQCp\nhcHBOZElxarNaVtkfJcJ5EDUUqEhS4VQuP/l/ISJiiXpDiBji513gBW2gYpl+znw\nF4FRdMxG5Ht9tfopFXc+hEUy1miV5YI428fZJnDLXSPeSIb3dKojymGe7S4EWqQH\nvFk6dzenaGxDAz1IdvOAza8jmpn8pjTvn3HoHtG0uQKBgQDaWKdcWl1jzWEy57II\nJziNPfFu+B3QKveWcn1gYuiqw1ny4BMi0ffQnMPzVsBdk+Rvkh3u9YBJPLOAnmme\nQfEiN8C6nZbgLfzEwfLjivhYumkTM5aWrpMNx7o8ghYctMtEInZYYvGfpk2X/mmQ\nD/XQxBxCIc69ZMkR3DhhLe7HJg==\n-----END PRIVATE KEY-----\n",
        "client_email": "firebase-adminsdk-iho5b@awaazproject-34fb8.iam.gserviceaccount.com",
        "client_id": "116536491936065302582",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-iho5b%40awaazproject-34fb8.iam.gserviceaccount.com"
    }
)



default_app = firebase_admin.initialize_app(cred)


#from firebase_admin import auth
#user = auth.get_user(uid)
#user.uid


def custom_firebase_authentication(request):
    auth_header = request.META.get("HTTP_AUTHORIZATION")
    if not auth_header:
        raise NoAuthToken("No auth token provided")

    id_token = auth_header.split(" ").pop()
    decoded_token = None
    try:
        #decoded_token = auth.verify_id_token(id_token)

        decoded_token = {"iss": "https://securetoken.google.com/awaazproject-34fb8","aud": "awaazproject-34fb8","auth_time": 1659516365,"user_id": "gQ1bbX9h6aNHLdbQ8FBFaYz3Bty1","sub": "gQ1bbX9h6aNHLdbQ8FBFaYz3Bty1","iat": 1659516365,"exp": 1659519965,"phone_number": "+918053838579","firebase": {"identities": {"phone": ["+918053838579"]},"sign_in_provider": "phone"}}
    except Exception:
        raise InvalidAuthToken("Invalid auth token")
    
    if not id_token or not decoded_token:
            print("jghm")
            return None

    try:
        uid = decoded_token.get("user_id")
    except Exception:
        raise FirebaseError()
    mobile_number = '+911234567890'
    try:
        mobile_number= decoded_token.get("phone_number")
    except Exception:
        pass
    signid_in_through = decoded_token.get("firebase")['sign_in_provider']
    user, created = User.objects.get_or_create(username=uid)
    if created:
        UserProfile.objects.create(last_activity=timezone.localtime(), user= user, mobile_number=mobile_number, signid_in_through=signid_in_through) 
        
    if user:
        return user
    else:
        return None
    

# class FirebaseAuthentication(authentication.BaseAuthentication):
#     def authenticate(self, request):
#         auth_header = request.META.get("HTTP_AUTHORIZATION")
#         if not auth_header:
#             raise NoAuthToken("No auth token provided")

#         id_token = auth_header.split(" ").pop()
#         decoded_token = None
#         try:
#             #decoded_token = auth.verify_id_token(id_token)

#             decoded_token = {"iss": "https://securetoken.google.com/awaazproject-34fb8","aud": "awaazproject-34fb8","auth_time": 1659516365,"user_id": "gQ1bbX9h6aNHLdbQ8FBFaYz3Bty1","sub": "gQ1bbX9h6aNHLdbQ8FBFaYz3Bty1","iat": 1659516365,"exp": 1659519965,"phone_number": "+918053838579","firebase": {"identities": {"phone": ["+918053838579"]},"sign_in_provider": "phone"}}
#         except Exception:
#             raise InvalidAuthToken("Invalid auth token")
#         # except Exception as e: # work on python 3.x
#         #     print("Exception is ", e)
#             pass

#         if not id_token or not decoded_token:
#             print("jghm")
#             return None

#         try:
#             uid = decoded_token.get("user_id")
#         except Exception:
#             raise FirebaseError()
#         mobile_number = '+911234567890'
#         try:
#             mobile_number= decoded_token.get("phone_number")
#         except Exception:
#             pass
#         signid_in_through = decoded_token.get("firebase")['sign_in_provider']
#         user, created = User.objects.get_or_create(username=uid)
#         if created:
#             UserProfile.objects.create(last_activity=timezone.localtime(), user= user, mobile_number=mobile_number, signid_in_through=signid_in_through) 

#         print("gxjasx", uid)
#         # authenticated = request.session.get('authenticated')
#         # request.session['authenticated_username']=uid
#         # if authenticated:
#         #     pass
#         # else:
#         #     request.session['authenticated']=True
#         # request.session['authenticated']=False
#         # auth_user = authenticate(username=uid)
#         # print(user)

#         #user.profile.last_activity = timezone.localtime()
#         return (user, None)

# class FirebaseAuthentication(authentication.BaseAuthentication):
#     def authenticate(self, request):
#         auth_header = request.META.get("HTTP_AUTHORIZATION")
#         if not auth_header:
#             raise NoAuthToken("No auth token provided")

#         id_token = auth_header.split(" ").pop()
#         firebase_username = id_token
#         #firebase_admin.initialize_app(cred)
#         try:
#             user = auth.get_user(firebase_username)
#         except Exception:
#             raise InvalidAuthToken()
#         #sign_in_provider = user.provider_id
#         mobile_number = user.phone_number
#         email = user.email
#         email_verified = user.email_verified
#         if mobile_number is None:
#             mobile_number = '+911234567890'
        
#         if email is None:
#             email = user.uid,"@awaaz.com"
#         print('Successfully fetched user data: {0}'.format(user.uid))

#         try:
#             uid = firebase_username
#         except Exception:
#             raise FirebaseError()
        

#         user, created = User.objects.get_or_create(username=uid)
#         user.email = email
#         user.save()
#         print("Created")
#         if created:
#             UserProfile.objects.create(last_activity=timezone.localtime(), user= user, mobile_number=mobile_number,email_verified=email_verified) 
#         return (user, None)