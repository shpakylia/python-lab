# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'task/post_list.html', {'posts': posts})
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'task/post_detail.html', {'post': post})




# Create your views here.
