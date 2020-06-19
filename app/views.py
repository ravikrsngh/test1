from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,HttpRequest,JsonResponse
from django.urls import reverse
from .models import *
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout,get_user_model
from django.contrib.auth.decorators import login_required
from datetime import datetime
import json
from django.contrib.auth.models import User
# Create your views here.
def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        birthday = request.POST.get('birthday')
        gender = request.POST.get('gender')
        try:
            image = request.FILES['image']
        except:
            image = None

        if User.objects.filter(username=email).exists():
            return HttpResponse("User Exists")
        user = User.objects.create(first_name = first_name , last_name =last_name , email = email , username = email)
        print("User Created")
        user.password = make_password(password)
        user.save();
        print("Password Set")
        userinfo.objects.create(user=user , birthday = birthday , gender = gender , profile_pic = image)
        print("UserInfo Added")
        return HttpResponseRedirect(reverse('app:home',args=(user.id,)))
    return render(request, 'signup.html',{})

def user_login(request):
    if request.method == "POST":
        username=request.POST.get('email')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            print("user has logged in \n\n\n")
            return HttpResponseRedirect(reverse('app:home',args=(user.id,)))
        else:
            print("Somebody logined but failed \n\n\n")
            return HttpResponseRedirect(reverse('app:signup'))
    else:
        return HttpResponseRedirect(reverse('app:signup'))

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('app:signup'))

def home(request , pk):
    all_users = userinfo.objects.all()
    user = User.objects.get(pk=pk)
    user_info = userinfo.objects.get(user=user)
    all_posts = post.objects.all().order_by('-time')
    all_comments = [];
    for i in all_posts:
        x = comments.objects.filter(post = i).order_by('-time')
        all_comments.append(x)
    print(all_comments)
    context = {
            'user' : user ,
            'user_info':user_info,
            'all_posts':all_posts,
            'all_users':all_users,
            'all_comments':all_comments,
    }
    return render(request,'home.html',context)

def makepost(request , pk):
    user = User.objects.get(pk=pk)
    user_info = userinfo.objects.get(user=user)
    if request.method == "POST":
        text = request.POST.get('text')
        try:
            picture= request.FILES['image']
        except:
            picture = None
        print(picture)
        try:
            video = request.FILES['video']
        except:
            video = None
        print(video)
        post.objects.create(user=user , user_info=user_info, text=text , photo = picture, videofile=video , l=0 , c=0,time=datetime.now())
        print("Post Created")
        return HttpResponseRedirect(reverse('app:home',args=(user.id,)))

def likepost(request):
    print(request.method)
    print("Going to like the post")
    post_id = request.GET['post_id']
    user_id = request.GET['user_id']
    p = post.objects.get(id=post_id)
    user = User.objects.get(pk=user_id)
    if likes.objects.filter(post = p).filter(user = user).exists():
        p.l = p.l - 1;
        likes.objects.filter(post = p).filter(user = user).delete()
        p.save()
        return HttpResponse(p.l)
    p.l = p.l +1;
    likes.objects.create(post = p , user = user)
    p.save()
    return HttpResponse(p.l)

def commentspost(request):
    post_id = request.GET['post_id']
    user_id = request.GET['user_id']
    print(user_id)
    body = request.GET['body']
    print(body)
    p = post.objects.get(pk=post_id)
    print("Hey1")
    user = User.objects.get(pk= user_id)
    print("Hey2")
    user_info = userinfo.objects.get(user=user)
    comments.objects.create(user = user , user_info = user_info , post=p , cmnt = body , time=datetime.now())
    p.c = p.c + 1;
    p.save()
    print("Comment Added")
    details = comments.objects.filter(post=p)
    list = []
    list.append(user.first_name)
    list.append(user.last_name)
    list.append(body)
    return JsonResponse(list , safe=False)

def profile(request , mypk , ppk):
    in_user = User.objects.get(pk=mypk)
    in_user_info = userinfo.objects.get(user = in_user)

    view_user = User.objects.get(pk=ppk)
    view_user_info = userinfo.objects.get(user = view_user)

    all_posts = post.objects.filter(user=view_user).order_by('-time')
    all_comments = [];
    for i in all_posts:
        x = comments.objects.filter(post = i).order_by('-time')
        all_comments.append(x)
    context = {
            'in_user' : in_user ,
            'in_user_info':in_user_info,
            'view_user':view_user,
            'view_user_info':view_user_info,
            'all_posts':all_posts,
            'all_comments':all_comments,
    }
    return render(request,'profile.html',context)

def cover_pic_change(request , pk):
    print("Entered Cover Pic Change")
    user = User.objects.get(pk=pk)
    user_info = userinfo.objects.get(user=user)
    cover_picture = request.FILES['cover_pic']
    user_info.cover_pic = cover_picture
    user_info.save()
    return HttpResponseRedirect(reverse('app:profile',args=(user.id,user.id,)))


def profile_pic_change(request , pk):
    print("Entered Profile Pic Change")
    user = User.objects.get(pk=pk)
    user_info = userinfo.objects.get(user=user)
    profile_picture = request.FILES['profile_pic']
    user_info.profile_pic = profile_picture
    user_info.save()
    return HttpResponseRedirect(reverse('app:profile',args=(user.id,user.id,)))

def addbio(request , pk):
    print("Entered Profile Pic Change")
    user = User.objects.get(pk=pk)
    user_info = userinfo.objects.get(user=user)
    bio = request.POST.get('bio')
    user_info.about = bio
    user_info.save()
    return HttpResponseRedirect(reverse('app:profile',args=(user.id,user.id,)))
