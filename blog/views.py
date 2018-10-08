from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Blog
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.views.generic import ListView, DetailView

class BlogList(ListView):
	model = Blog

class BlogDetail(DetailView):
	model = Blog	

def index(request):
	latest_blogs = Blog.objects.order_by('-pub_date')
	context = {'latest_blogs': latest_blogs}
	return render(request, 'blog/index.html', context)

def detail(request, blog_id):
	blog = get_object_or_404(Blog, pk = blog_id)
	return render(request, 'blog/detail.html', {'blog' : blog,})

def new(request):
	if request.method == "GET":
		if not request.user.is_authenticated:
			return render(request,'blog/signup.html',{})
		else:
			return render(request,'blog/new.html',{})
	elif request.method == 'POST':
		print("new ke POST mein")
		title = request.POST.get("title","")
		content = request.POST.get("content","")
		current_user = request.user
		author = current_user.username
		if len(title) != 0 and len(content) != 0:
			new_blog = Blog(blog_title = title, blog_content = content, blog_author = author, pub_date=timezone.now())
			new_blog.save()
			return HttpResponseRedirect(reverse('blog:detail', args = (new_blog.id,)))
		else:
			return render(request,'blog/new.html',{})

def signUp(request):
	if request.method == "GET":
		return render(request,'blog/signup.html',{})
	elif request.method == 'POST':
		username = request.POST.get("username","")
		email = request.POST.get("email","")
		password = request.POST.get("password","")
		if len(email) != 0 and len(password) != 0 and len(username) != 0:
			user = authenticate(request, username=username, password=password)
			if user is not None:	# old user
				login(request, user)
			else:					# new user
				newUser = User.objects.create_user(username, email, password)
				login(request,newUser)
			
			return HttpResponseRedirect(reverse('blog:index'))
		else:						# something wrong
			return render(request,'blog/signup.html',{})

def logoutUser(request):
	logout(request)
	return HttpResponseRedirect(reverse('blog:index'))

def signIn(request):
	if request.method == "GET":
		return render(request,'blog/signin.html',{})
	elif request.method == 'POST':
		username = request.POST.get("username","")
		password = request.POST.get("password","")
		if len(password) != 0 and len(username) != 0:
			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)
				return HttpResponseRedirect(reverse('blog:index'))
			else:
				return HttpResponseRedirect(reverse('blog:signUp'))
		else:						# incorrect input
			return render(request,'blog/signin.html',{})

def updateBlog(request, blog_id):
	blog = get_object_or_404(Blog, pk = blog_id)
	if request.method == "GET":
		if blog.blog_author == request.user.username:
			print(blog.id)
			return render(request,'blog/updateblog.html', {'blog' : blog,})
		else :
			return render(request, 'blog/detail.html', {'blog' : blog,})
	elif request.method == 'POST':
		print("update ke POST mein")
		title = request.POST.get("title","")
		content = request.POST.get("content","")
		current_user = request.user
		author = current_user.username
		if len(title) != 0 and len(content) != 0:
			print("inside if")
			updated_blog = Blog.objects.get(pk = blog_id)
			updated_blog.blog_title = title
			updated_blog.blog_content = content
			updated_blog.save()
			return HttpResponseRedirect(reverse('blog:detail', args = (updated_blog.id,)))

def deleteBlog(request, blog_id):
	blog = get_object_or_404(Blog, pk = blog_id)
	if request.method == "GET":
		if blog.blog_author == request.user.username:
			blog_to_delete = Blog.objects.get(pk = blog_id)
			blog_to_delete.delete()
			return HttpResponseRedirect(reverse('blog:index'))
		else :
			return render(request, 'blog/detail.html', {'blog' : blog,})



