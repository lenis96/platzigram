from django.shortcuts import render,redirect
from datetime import datetime
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from posts.models import Post

from posts.forms import PostForm


@login_required
def list_posts(request):
    posts=Post.objects.all().order_by('created')
    return render(request,'posts/feed.html',{'posts':posts})

@login_required
def create_post(request):
    if(request.method=='POST'):
        form=PostForm(request.POST,request.FILES)
        if(form.is_valid()):
            form.save()
            return redirect('feed')
    else:
        form=PostForm()
    return render(request,'posts/new.html',{
        'form':form,
        'user':request.user,
        'profile':request.user.profile
    })