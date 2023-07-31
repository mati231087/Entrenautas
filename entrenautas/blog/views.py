from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list_view(request):
    posts = Post.objects.filter(published_date__isnull=False).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def index(request):
    return render(request, 'blog/index.html')

def about(request):
    return render(request, 'blog/about.html', {})

# Create your views here.
