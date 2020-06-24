# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.core.paginator import Paginator
import re
import math


# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    total_pages = int(math.ceil(posts.count() / 5.0))

    if page_number is None:
        page_number = 1
    else:
        page_number = int(page_number)
        if page_number < 1:
            page_number = 1

        if total_pages < page_number:
            if total_pages < 1:
                page_number = 1
            else:
                page_number = total_pages

    page_obj = paginator.page(page_number)

    return render(request, 'blog/post_list.html',
                  {'posts': page_obj, 'url': "blog", 'page': page_number, 'pg_total': total_pages,
                   'pg_array': range(1, total_pages + 1, 1)})


def post_full(request):
    path = request.path.split("/")
    if request.path.endswith("/"):
        id = path[len(path) - 2]
    else:
        id = path[len(path) - 1]
    if re.match('[0-9]+', id):
        post = Post.objects.filter(id=int(id))
        if len(post) > 0:
            final_post = post[0]
        else:
            final_post = None

        return render(request, 'blog/post.html',
                      {'post': final_post})
    else:
        return render(request, 'blog/post.html',
                      {'post': None, 'url': "blog"})
