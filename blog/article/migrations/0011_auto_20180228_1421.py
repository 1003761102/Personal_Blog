# Generated by Django 2.0 on 2018-02-28 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0010_articlemodel_add_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlemodel',
            name='add_time',
            field=models.DateTimeField(),
        ),
    ]
