# Generated by Django 2.0 on 2018-02-02 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_articlemodel_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlemodel',
            name='auther',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='作者'),
        ),
    ]