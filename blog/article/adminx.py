import xadmin
from xadmin import views
from .models import ArticleModel, TagModel, CategoryModel


class GlobalSetting(object):
    site_title = 'clean blog v.1.0'
    site_footer = 'my blog'

xadmin.site.register(views.CommAdminView, GlobalSetting)


class ArticleAdmin(object):
    list_display = ['title', 'category', 'tags', 'body', 'image', 'click_nums', 'comment_nums', ]
    search_fields = ['title', 'category', 'tags', 'body', 'image', 'click_nums', 'comment_nums']
    list_filter = ['title', 'category', 'tags', 'body', 'image', 'click_nums', 'comment_nums', ]


class TagAdmin(object):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']


class CategoryAdmin(object):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']


xadmin.site.register(ArticleModel, ArticleAdmin)
xadmin.site.register(TagModel, TagAdmin)
xadmin.site.register(CategoryModel, CategoryAdmin)
# xadmin.site.register(OnlineEditorModel)









