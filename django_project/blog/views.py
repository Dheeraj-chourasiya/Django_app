from dataclasses import fields
from pyexpat import model
from urllib import request
from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin


# Create your views here.
#this function is the logic to handle when someone going to blog homepage of our app
posts=[
    {
         'Authors':'Dheeraj',
         'title':'Blog post 1',
         'content':'first Blog content',
         'date_posted':'April 22, 2022'
    },
    {
        'Authors':'Dev',
        'title':'Blog post 2',
         'content':'second Blog content',
         'date_posted':'April 23, 2022'
    }
]


def home(request):# to get this function working passing request object but we are not using this now.
    context={'posts':Post.objects.all()}
    return render(request,'blog/home.html', context)

class PostListView(ListView):
    model=Post   #in order to use this open blog/urls.py and say thatwe wantto use Listvew 
    template_name = 'blog/home.html' # by default is is looking in app/model_vietype.html but here we have change that
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class UserPostListView(ListView):
    model=Post    
    template_name = 'blog/user_post.html' 
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(authors=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post    

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content']   
   
    def form_valid(self,form):
       form.instance.authors = self.request.user
       return super().form_valid(form) 


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title','content']   

    def form_valid(self,form):
       form.instance.authors = self.request.user
       return super().form_valid(form) 

    def test_func(self):
        post = self.get_object()  # this function prevent other user to to update or delete other user post
        if self.request.user== post.authors:
            return True  
        return False     

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post 
    success_url = '/'  

    
    def test_func(self):
        post = self.get_object()  
        if self.request.user== post.authors:
            return True  
        return False              

def about(request):# to get this function working passing request object but we are not using this now.
     return render(request,'blog/about.html',{'title':'About'})