# Generated by Django 2.0 on 2018-02-02 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='标签')),
            ],
            options={
                'verbose_name': '标签',
                'verbose_name_plural': '标签',
            },
        ),
        migrations.RemoveField(
            model_name='articlemodel',
            name='tags',
        ),
        migrations.AlterField(
            model_name='categorymodel',
            name='name',
            field=models.CharField(max_length=10, verbose_name='分类'),
        ),
        migrations.AddField(
            model_name='articlemodel',
            name='tags',
            field=models.ManyToManyField(to='article.TagModel', verbose_name='标签'),
        ),
    ]