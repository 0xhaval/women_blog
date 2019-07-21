from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

def test(request):
    data = Article.objects.all().order_by('date')
    context = {'article':data}
    return render(request,'article/article.html',context)

def article_detail(request,slug):
    article = Article.objects.get(slug=slug)
    return render(request,'article/article_detail.html',{'article':article})
