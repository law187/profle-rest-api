from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Post
from django.contrib.auth.decorators import login_required



def home(request):

    #all = Post.objects

    return render(request,'post/home.html')
