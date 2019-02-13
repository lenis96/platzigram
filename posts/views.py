from django.shortcuts import render,redirect
from datetime import datetime
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView,DetailView,CreateView
from django.urls import reverse_lazy

from posts.models import Post

from posts.forms import PostForm

class PostsFeedView(LoginRequiredMixin,ListView):
    template_name='posts/feed.html'
    model=Post
    ordering=('-created',)
    paginate_by=20
    context_object_name='posts'

class PostDetailView(LoginRequiredMixin,DetailView):
    template_name='posts/detail.html'
    queryset=Post.objects.all()
    context_object_name='post'

class CreatePostView(LoginRequiredMixin,CreateView):
    template_name='posts/new.html'
    form_class=PostForm
    success_url=reverse_lazy('posts:feed')

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['user']=self.request.user
        context['profile']=self.request.user.profile
        return context

@login_required
def list_posts(request):
    posts=Post.objects.all().order_by('-created')
    return render(request,'posts/feed.html',{'posts':posts})

@login_required
def create_post(request):
    if(request.method=='POST'):
        form=PostForm(request.POST,request.FILES)
        if(form.is_valid()):
            form.save()
            return redirect('posts:feed')
    else:
        form=PostForm()
    return render(request,'posts/new.html',{
        'form':form,
        'user':request.user,
        'profile':request.user.profile
    })