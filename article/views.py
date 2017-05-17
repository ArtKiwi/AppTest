from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext, context, Template
from article.models import Article, Comments
from django.core.exceptions import ObjectDoesNotExist
from article.forms import CommentForm, ArticleForm
from django.template.context_processors import csrf
from django.contrib.auth.context_processors import auth
from django.contrib import auth
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required, permission_required


def articles(request):
    all_articles = Article.objects.all()
    paginator = Paginator(all_articles, 5)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    return render(request, 'articles.html', {'articles': articles})


def article(request, article_id=1):
    comment_form = CommentForm
    args = {}
    args.update(csrf(request))
    args['article'] = Article.objects.get(id=article_id)
    args['comments'] = Comments.objects.filter(comments_arcticle_id=article_id)
    args['form'] = comment_form
    return render(request, 'article.html', args)


def addlike(request, article_id):
    return_path = request.META.get('HTTP_REFERER', '/')  # save link
    try:
        if article_id in request.COOKIES:
            redirect(return_path)
        else:
            article = Article.objects.get(id=article_id)
            article.article_likes += 1
            article.save()
            response = redirect(return_path)
            response.set_cookie(article_id, 'like')
            return response
    except ObjectDoesNotExist:
        raise http404
    return redirect(return_path)


@login_required
def addcomment(request, article_id):
    if request.POST and ('pause' not in request.session):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_arcticle = Article.objects.get(id=article_id)
            form.save()
            request.session.set_expiry(60)
            request.session['pause'] = True
    return redirect('/articles/get/%s/' % article_id)


@permission_required('article.add_article')
def addarticle(request):
    form = ArticleForm()
    if request.POST:
        addform = ArticleForm(request.POST)
        if addform.is_valid():
            addform.save()
    return render(request, 'addarticle.html', {'form': form})


@permission_required('article.change_article')
def editarticle(request, id):
    article = Article.objects.get(id=id)
    form = ArticleForm(instance=article)
    if request.POST:
        changeform = ArticleForm(request.POST, instance=article)
        if changeform.is_valid():
            changeform.save()
            return redirect('/')
    return render(request, 'editarticle.html', {'form': form, 'article': article})
