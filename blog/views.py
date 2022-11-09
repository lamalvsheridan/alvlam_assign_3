from django.shortcuts import render
from . import models

# Create your views here.
def home(request):
    """
    The Blog homepage
    """
    return render(
        request,
        'blog/home.html'
    )
