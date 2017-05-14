from django.contrib import admin
from article.models import Article, Comments
from django_summernote.admin import SummernoteModelAdmin


class ArticleInLine(admin.StackedInline):
    model = Comments
    extra = 2


class Article_Admin(SummernoteModelAdmin):
    fields = ['article_title', 'article_text']
    inlines = [ArticleInLine]
    list_filter = ['article_date']


admin.site.register(Article, Article_Admin)
