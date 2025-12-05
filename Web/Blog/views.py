from django.shortcuts import render,redirect,get_object_or_404
from .models import Post,User
from .forms import LoginForm,CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.contrib.auth.decorators import login_required


class PostView(ListView):
    model = Post
    template_name = 'blog.html'  
    
class BlogView(DetailView):
    model=Post
    template_name='blogdetail.html'  
           
def loginPage(request):
    form=LoginForm()
    if request.method=="POST":
        form=LoginForm(request.POST)
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("blog")
            
    context={'form':form}
    return render(request, 'login.html',context)

def sign_up(request):
    form=CreateUserForm()
    if request.method == "POST":
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("loginPage")

    context={'form':form}
    return render(request,'signup.html', context)

def index(request):
    return render(request,'index.html')

def blog(request):
    posts=Post.objects.all().order_by('-Date_created')
    context= {
        "posts":posts,
    }
    return render(request,"blog.html",context=context)

def blog_detail(request, pk):
    posts=Post.objects.get(pk=pk)
    context= {
        "posts":posts,
    }    
    return render(request,"blogdetail.html",context)   
 
@login_required
def logout(request):
     
    auth.logout(request)
    
    return redirect("loginPage")

