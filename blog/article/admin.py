from ckeditor_uploader import utils
from django.contrib import admin
# Register your models here.
from .models import ArticleModel, CategoryModel, TagModel


class ArtilceAdmin(admin.ModelAdmin):
    # list_display = ['title', 'category', 'tags', 'body', 'image', 'click_nums', 'comment_nums', 'add_time']
    # search_fields = ['title', 'category', 'tags', 'body', 'image', 'click_nums', 'comment_nums']
    # list_filter = ['title', 'category', 'tags', 'body', 'image', 'click_nums', 'comment_nums', 'add_time']
    #
    #
    pass


class CategoryAdmin(admin.ModelAdmin):
    pass


class TagAdmin(admin.ModelAdmin):
    pass


admin.site.register(ArticleModel, ArtilceAdmin)
admin.site.register(TagModel, TagAdmin  )
admin.site.register(CategoryModel, CategoryAdmin)
# admin.site.register(OnlineEditorModel)
utils