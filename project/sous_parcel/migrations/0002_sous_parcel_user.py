# Generated by Django 4.1.7 on 2023-04-06 15:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sous_parcel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sous_parcel',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='conv', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]