# Generated by Django 4.1.7 on 2023-05-23 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0008_profile_nakwa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]