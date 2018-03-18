from django.shortcuts import render

# Create your views here.
from django.views import View
from .models import CategoryModel, ArticleModel, TagModel


class HomeView(View):
    def get(self, request):
        all_articles = ArticleModel.objects.all()
        all_articles = all_articles.order_by('-add_time')
        hot_articles = all_articles.order_by('-comment_nums')[0:5]
        click_articles = all_articles.order_by('-click_nums')[0:5]
        for article in all_articles:
            print(article.title)
            print(article.tags.all())
        context = {
            'all_articles': all_articles,
            'hot_articles': hot_articles,
            'click_articles': click_articles
        }
        return render(request, 'index.html', context)


class ArticleListView(View):
    def get(self, request):
        all_articles = ArticleModel.objects.all()
        all_articles = all_articles.order_by('-add_time')
        hot_articles = all_articles.order_by('-comment_nums')[0:5]
        click_articles = all_articles.order_by('-click_nums')[0:5]
        print(all_articles)
        for article in all_articles:
            print(article.title)
            print(article.tags.all())
        context = {
            'all_articles': all_articles,
            'hot_articles': hot_articles,
            'click_articles': click_articles
        }
        return render(request, 'article.html', context)


class jishuzatanView(View):
    def get(self, request):
        all_articles = ArticleModel.objects.all()
        all_articles = all_articles.order_by('-add_time')
        hot_articles = all_articles.order_by('-comment_nums')[0:5]
        click_articles = all_articles.order_by('-click_nums')[0:5]
        for article in all_articles:
            print(article.title)
            print(article.tags.all())
        context = {
            'all_articles': all_articles,
            'hot_articles': hot_articles,
            'click_articles': click_articles
        }
        return render(request, 'jishuzatan.html', context)


class AboutmeView(View):
    def get(self, request):
        return render(request, 'about.html')


class ArticleDetailView(View):
    def get(self, request, id):
        articles = ArticleModel.objects.get(id=int(id))
        all_articles = ArticleModel.objects.all()
        all_articles = all_articles.order_by('-add_time')
        hot_articles = all_articles.order_by('-comment_nums')[0:5]
        click_articles = all_articles.order_by('-click_nums')[0:5]
        context = {
            'articles': articles,
            'all_articles': all_articles,
            'hot_articles': hot_articles,
            'click_articles': click_articles
        }
        return render(request, 'article_detail.html', context)

