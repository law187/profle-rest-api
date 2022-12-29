from django.shortcuts import render, get_object_or_404
from django.http import Http404
from . import models
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone
from django.http import HttpResponse


@login_required
def create(request):
    error='you have added it'
    if request.method =='POST':
        if request.POST['title'] and request.POST['body']:
             post = models.Post()
             post.title = request.POST['title']
             post.body = request.POST['body']
             post.author = request.user
             post.date = timezone.datetime.now()
             if len(request.FILES) != 0:
                 post.image=request.FILES['image']

             post.save()
             return render(request,'post/create.html',{'error':error})

    else:
        return render(request,'post/create.html')




def home(request):

        all=models.Post.objects


        return render(request,'post/home.html',{'all':all})

@login_required
def details(request,id):

        all=models.Post.objects.get(pk=id)


        return render(request,'post/details.html',{'all':all})
