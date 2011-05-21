from django.http import HttpResponse
from django.shortcuts import render_to_response

from myblog import models

def home(request):
    articles = models.Article.objects.all().order_by('-updated')
    return render_to_response('myblog/index.html', {'articles': articles})

def article(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render_to_response('myblog/article.html', {'article': article})