# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Post
from django.utils import timezone
from django.shortcuts import render
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'task/post_list.html', {'posts': posts})



# Create your views here.
