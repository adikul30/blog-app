from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Blog
from django.utils import timezone
from django.urls import reverse

def index(request):
	latest_blogs = Blog.objects.order_by('-pub_date')[:5]
	context = {'latest_blogs': latest_blogs}
	return render(request, 'blog/index.html', context)

def detail(request, blog_id):
	blog = get_object_or_404(Blog, pk = blog_id)
	return render(request, 'blog/detail.html', {'blog' : blog,})

def new(request):
	if request.method == "GET":
		return render(request,'blog/new.html',{})
	elif request.method == 'POST':
		title = request.POST.get("title","")
		content = request.POST.get("content","")
		author = request.POST.get("author","")
		new_blog = Blog(blog_title = title, blog_content = content, blog_author = author, pub_date=timezone.now())
		new_blog.save()
		print(new_blog.id)
		return HttpResponseRedirect(reverse('blog:detail', args = (new_blog.id,)))