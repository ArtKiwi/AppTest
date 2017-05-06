from django.contrib import admin
from article.models import Article, Comments


class ArticleInLine(admin.StackedInline):
    model = Comments
    extra = 2


class Article_Admin(admin.ModelAdmin):
    fields = ['article_title', 'article_text', 'article_date']
    inlines = [ArticleInLine]
    list_filter = ['article_date']


admin.site.register(Article, Article_Admin)
