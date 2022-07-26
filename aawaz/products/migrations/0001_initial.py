# Generated by Django 3.2.14 on 2022-08-02 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product_type', models.CharField(choices=[('coin', 'Coin'), ('gift', 'Gift'), ('diamond', 'Diamond')], max_length=50)),
                ('product_name', models.CharField(max_length=120)),
                ('product_image', models.ImageField(upload_to='upload/products/')),
                ('product_price', models.FloatField(default=0.0)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
