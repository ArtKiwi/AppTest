# -*- coding: utf-8 -*-
from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
# Create your models here.


class Article (models.Model):
    article_title = models.CharField(max_length=200)
    article_text = models.TextField()
    article_date = models.DateTimeField()
    article_likes = models.IntegerField(default=0)
    count_comments = models.IntegerField(default=0)

    def __str__(self):
        return self.article_title

class Comments (models.Model):
    comments_text = models.TextField(verbose_name="Текст комментария:")
    comments_arcticle = models.ForeignKey (Article)

@receiver(post_save, sender = Comments)
def add_count (instance, **kwargs):
    count = instance.comments_arcticle
    count.count_comments += 1
    count.save()

@receiver(post_delete, sender = Comments)
def reduce_count (instance, **kwargs):
    profile = instance.comments_arcticle
    profile.count_comments -= 1
    profile.save()
