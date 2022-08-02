from django.shortcuts import render, HttpResponse
import  datetime
# Create your views here.

def index(request):
    return render(request, "index.html",)
