# Generated by Django 2.2.10 on 2020-10-28 19:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20201028_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='writer',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]