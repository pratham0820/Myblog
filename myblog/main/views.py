from django.shortcuts import render
from django.http import HttpResponse
from main.models import Post,Category

# Create your views here.



def home (request):
    posts = Post.objects.all()[:11]

    cats = Category.objects.all()

    data = {
           'cats':cats,
           'posts':posts
    }
    return render(request,'home.html', data)

def post(request,url):
    post = Post.objects.get(url=url)
    return render(request,'posts.html',{'post':post})


def category(request,url):
    cats = Category.objects.get(url=url)
    return render(request,'category.html',{'cats':cats})

