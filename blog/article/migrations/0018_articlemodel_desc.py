# Generated by Django 2.0 on 2018-02-28 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0017_articlemodel_add_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlemodel',
            name='desc',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='摘要'),
        ),
    ]
