# Generated by Django 4.1.7 on 2023-04-20 00:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sous_parcel', '0014_alter_sous_parcel_parcel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sous_parcel',
            name='slug',
        ),
    ]
