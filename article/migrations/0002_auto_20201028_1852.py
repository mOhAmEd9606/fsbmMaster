# Generated by Django 2.2.10 on 2020-10-28 18:52

import ckeditor.fields
import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='catid',
            new_name='catID',
        ),
        migrations.AlterField(
            model_name='article',
            name='artbody',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='article',
            name='cat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='article.Cat'),
        ),
        migrations.AlterField(
            model_name='article',
            name='discripton',
            field=ckeditor.fields.RichTextField(),
        ),
    ]