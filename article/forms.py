# -*- coding: utf-8 -*-
from django.forms import ModelForm
from article.models import Comments, Article
from django.db import models
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['comments_text']


class ArticleForm(ModelForm):
    article_text = models.TextField(SummernoteWidget())

    class Meta:
        model = Article
        fields = ['article_title', 'article_text']
        widgets = {
            'foo': SummernoteWidget(),
            'bar': SummernoteInplaceWidget(),
        }
