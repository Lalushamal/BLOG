from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Post
from . forms import MakePost
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def index(request):
    post = {
        'post':Post.objects.all()
    }
    return render(request,'index.html',post)

def blog(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request,'blog.html',{'post':post})
def delete(request,post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('index')
@login_required 
def create(request):
    if request.method == 'POST':
        form = MakePost(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return index(request)
    return render(request,'create.html',{'form':MakePost()})
def update(request,post_id):
    post = Post.objects.get(id=post_id)
    form = MakePost(instance=post)
    if request.method == 'POST':
        form = MakePost(request.POST,request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'update.html', {'form': form})

def register(request):
    form=UserCreationForm()
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts/login')
    return render(request,'register.html',{'form': form})

