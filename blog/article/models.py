from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from  ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class CategoryModel(models.Model):
    name = models.CharField(max_length=10, verbose_name='分类')

    class Meta:
        verbose_name = '文章类别'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class TagModel(models.Model):
    name = models.CharField(max_length=10, verbose_name='标签')

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class ArticleModel(models.Model):
    title = models.CharField(max_length=50, verbose_name='标题')
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, verbose_name='文章类别')
    tags = models.ManyToManyField(TagModel, verbose_name='标签')
    auther = models.CharField(max_length=10, verbose_name='作者', null=True, blank=True)
    desc = models.TextField(max_length=100, verbose_name='摘要', null=True, blank=True)
    body = RichTextUploadingField(verbose_name='content', config_name='default')
    image = models.ImageField(upload_to='image/article/%Y/%m', verbose_name='头像')
    click_nums = models.IntegerField(default=0, verbose_name='浏览量')
    comment_nums = models.IntegerField(default=0, verbose_name='评论量')
    add_time = models.DateTimeField(default=datetime.now,  verbose_name='添加时间')

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title



