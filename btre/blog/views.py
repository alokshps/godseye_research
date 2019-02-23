from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
# def post_list(request):
#     return render(request, 'blog/post_list.html',{})

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = Post.objects.filter(is_published=True)

    return render(request, 'blog/post_list.html', {'posts': posts})

def post(request):
 return render(request,'blog/post.html')

