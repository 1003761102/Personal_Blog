# Generated by Django 2.0 on 2018-02-28 07:21

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0013_onlineeditormodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlemodel',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='content'),
        ),
    ]