# Generated by Django 2.2.10 on 2020-10-28 18:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20201028_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='writer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
