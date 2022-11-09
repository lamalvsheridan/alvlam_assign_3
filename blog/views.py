from django.shortcuts import render
from django.db.models import Count
from . import models

# Create your views here.
def home(request):
    """
    The Blog homepage
    """
    latest_posts = models.Post.objects.published().order_by('-published')[:3]
    topics = models.Topic.objects.annotate(Count('blog_posts')).order_by('-blog_posts__count')[:10]

    context = {
        'topics': topics,
        'latest_posts': latest_posts
    }

    return render(request, 'blog/home.html', context)
