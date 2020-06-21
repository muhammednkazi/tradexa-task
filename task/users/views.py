# in this file we write functions for the urls entered.

from django.shortcuts import render,redirect
from .models import user
from .models import posts
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def index(request):
    # if User.is_authenticated:
    #     return redirect('blogs')
    # else:
    return render(request,'users/index.html')

def signup(request):
    if request.method == "POST":
        first_name = request.POST.get('firstname', '')
        last_name = request.POST.get('lastname', '')
        email = request.POST.get('email', '')
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        cpassword = request.POST.get('cpassword', '')

        if password!=cpassword:
            messages.error(request,'Passwords Should Be Same')
            return redirect('signup')
        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = first_name
        myuser.last_name = last_name
        myuser.save()
        messages.success(request, 'New User Created Successfully.')
        return redirect('login')
        # myuser.success(request,"Your Account has Been Created")
    return render(request,'users/signup.html')

def userlogin(request):
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        check=authenticate(username=username,password=password)
        if check is not None:
            login(request,check)
            messages.success(request,'Login Successful')
            return redirect('blogs')
        else:
            messages.error(request,'Invalid Credentials. Please try Again!')
            return redirect('userlogin')
        # if username=='' or password=='':
        #     messages.error(request, 'Please fill the form correctly.')
        # else:
        #     # messages.success(request, 'Please fill the form correctly.')
        #     pass
    return render(request,'users/userlogin.html')

def userlogout(request):
    logout(request)
    messages.success(request,"You are Logged Out!")
    return render(request,'users/index.html')

def blogs(request):
    posts_data= posts.objects.all()
    param = {'posts_data': posts_data}
    return render(request, 'users/blogs.html', param)


def addpost(request):
    if request.method == "POST":
        title = request.POST.get('title', '')
        text = request.POST.get('text', '')
        if title=='' or text=='':
            messages.error(request, 'Please fill the form correctly.')
        else:
            data = posts(title=title, text=text,postinguser=request.user)
            data.save()
            messages.success(request, 'Post Upload Successfully.')
    return render(request,'users/addpost.html')

def blogpost(request,id):
    posts_data= posts.objects.filter(posts_id=id)[0]
    param = {'posts_data': posts_data}
    return render(request, 'users/blogpost.html', param)