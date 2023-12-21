from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    latest = Post.objects.order_by('-pub_date')[0:3]
    return render(request, 'home.html', {'latest': latest})

def blog(request):
    posts = Post.objects.all()
    return render(request,'blog.html', {'posts': posts})

def detail_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'post_detail.html', {'post': post})


@login_required
def dashboard(request):
    posts = Post.objects.all()
    return render(request, "dashboard.html", {'posts':posts})

@login_required
def create_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        thumbnail = request.FILES['thumbnail']
        Post.objects.create(title=title, content=content, thumbnail=thumbnail)
        return redirect('dashboard')
    return render(request, "create_post.html")


@login_required
def update_post(request, post_id):
    post = get_object_or_404(Post, id = post_id)
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        thumbnail = request.FILES.get('thumbnail', post.thumbnail)

        Post.objects.filter(id = post_id).update(title=title, content=content, thumbnail=thumbnail)
        return redirect('dashboard')
    return render(request, "update_post.html", {'post':post})


@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id = post_id)
    post.delete()
    return redirect('dashboard')
