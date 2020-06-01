from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from .models import Post

def display_index(request):
    post_list = Post.objects.order_by('-created')[:5]
    return render(
        request,
        "blogapp/index.html",
        {'post_list': post_list}
    )

def display_archive(request):
    post_list = Post.objects.order_by('-created')
    return render(
        request,
        "blogapp/archive.html",
        {'post_list': post_list}
    )

def display_about(request):
    return render(
        request,
        "blogapp/about.html"
    )

def display_post(request, post_url):
    post = get_object_or_404(Post, url=post_url)
    return render(
        request,
        'blogapp/display.html',
        {'post': post}
    )
