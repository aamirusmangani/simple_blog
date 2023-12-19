from django.shortcuts import render, get_object_or_404, redirect
from .models import Post

# Create your views here.

def home(request):
    latest = Post.objects.order_by('-pub_date')[0:3]
    return render(request, 'home.html', {'latest': latest})