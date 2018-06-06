# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import redirect
from .models import Post
from django.contrib.auth.models import User
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
import re
import string
import collections
from operator import itemgetter

def post_list(request):

    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    new_posts = []
    def special_characters(data):
        regexp = '[{}]*'.format(string.punctuation)
        return re.sub(regexp, '', text)

    for i, post in enumerate(posts):
        counter = collections.Counter()
        text = post.text
        for word in special_characters(text).split():
            counter[word] += 1
        post.uniq = len(counter)
        new_posts.append(post)
        # new_posts[i]['uniq'] = len(counter)
    # new_posts = sorted(new_posts, key=itemgetter('uniq'), reverse=True)
    new_posts = sorted(new_posts, key=lambda k: k.uniq, reverse=True)
    return render(request, 'task/post_list.html', {'posts': new_posts})
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'task/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            demo = User.objects.get(username='demo')
            post.author = demo
            post.published_date = timezone.now()
            post.save()
            return redirect('post_dlist')
    else:
        form = PostForm()
        return render(request, 'task/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            demo = User.objects.get(username='demo')
            post.author = demo
            post.published_date = timezone.now()
            post.save()
            return redirect('post_list')
    else:
        form = PostForm(instance=post)
        return render(request, 'task/post_edit.html', {'form': form})


# Create your views here.
