# Generated by Django 2.0 on 2018-02-28 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0018_articlemodel_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlemodel',
            name='image',
            field=models.ImageField(upload_to='image/article/%Y/%m', verbose_name='头像'),
        ),
    ]
