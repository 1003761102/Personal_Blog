# Generated by Django 2.0 on 2018-02-02 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_articlemodel_auther'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlemodel',
            name='image',
            field=models.ImageField(upload_to='media/image/article/%Y/%m', verbose_name='头像'),
        ),
    ]