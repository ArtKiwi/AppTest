from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext, context, Template
from article.models import Article, Comments
from django.core.exceptions import ObjectDoesNotExist
from article.forms import CommentForm
from django.template.context_processors import csrf
from django.contrib import auth
from django.core.paginator import Paginator
from django.http import HttpRequest

# Create your views here.
def articles (request, page_number=1):
#   args = {}
#   args ['comments'] = Comments.objects.count()
    all_articles = Article.objects.all()
    current_page = Paginator(all_articles, 5)
    return render_to_response ('articles.html',
    {'articles': current_page.page(page_number),'username': auth.get_user(request).username})
def article (request, article_id=1):
    comment_form = CommentForm
    args ={}
    args.update (csrf(request))
    args['article']=Article.objects.get(id=article_id)
    try:
        args['comments']=Comments.objects.filter (comments_arcticle_id=article_id)
    except args['comments'].DoesNotExist:
        args['comments'] = None
    args ['form']=comment_form
    args['username']= auth.get_user(request).username
    args ['count_comments'] =Comments.objects.get(id=article_id)
    return render_to_response ('article.html', args)

    #eturn render_to_response ('article.html', {'article' : Article.objects.get(id=article_id), 'comments': Comments.objects.filter (comments_arcticle_id=article_id)})
def addlike(request, article_id ):
    return_path  = request.META.get('HTTP_REFERER','/') # сохраняет предыидущую ссылку

    try:
        if article_id in request.COOKIES:
            redirect (return_path )
        else:
            article = Article.objects.get(id=article_id)
            article.article_likes +=1
            article.save ()
            response = redirect(return_path)
            response.set_cookie(article_id, 'like')
            return response
    except ObjectDoesNotExist:
        raise http404
    return redirect (return_path)

def addcomment (request, article_id):
    if request.POST and ('pause' not in request.session):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save (commit=False)
            comment.comments_arcticle = Article.objects.get(id=article_id)
            form.save()
            count=Article.objects.get(id=article_id)
            count.count_comments +=1
            count.save ()
            request.session.set_expiry(60)
            request.session ['pause'] = True
    return redirect('/articles/get/%s/' % article_id)

