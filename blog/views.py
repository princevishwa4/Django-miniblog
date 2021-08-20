from blog.forms import RegisterForm, LoginForm, BlogForm
from blog.models import BlogPost
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.shortcuts import render, HttpResponseRedirect


def home(request):
	blogs = BlogPost.objects.all()
	return render(request, 'blog/home.html', {'blogs' : blogs})


def about(request):
	return render(request, 'blog/about.html')


def contact(request):
	return render(request, 'blog/contact.html')


def dashboard(request):
	if request.user.is_authenticated:
		blogs = BlogPost.objects.all()
		return render(request, 'blog/dashboard.html', {'blogs' : blogs})
	else:
		return HttpResponseRedirect('/login')


def user_login(request):
	if not request.user.is_authenticated:
		if request.method == "POST":
			form = LoginForm(request=request, data=request.POST)
			if form.is_valid():
				username = form.cleaned_data['username']
				password = form.cleaned_data['password']
				user = authenticate(username=username, password=password)
				if user is not None:
					messages.success(request, 'Logged in Successfully')
					login(request, user)
					return HttpResponseRedirect('/dashboard')
		else:
			form = LoginForm()
		return render(request, 'blog/login.html', {'form' : form})
	else:
		return HttpResponseRedirect('/dashboard')


def user_register(request):
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			messages.success(request, "You have become an Author in our Blog Site!!")
			user = form.save()
			group = Group.objects.get(name='Author')
			user.groups.add(group)
	else:
		form = RegisterForm()
	return render(request, 'blog/register.html', {'form': form})


def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/')


def add_blog(request):
	if request.user.is_authenticated:
		if request.method == "POST":
			form = BlogForm(request.POST)
			if form.is_valid():
				title = form.cleaned_data['title']
				description = form.cleaned_data['description']
				formData = BlogPost(title=title, description=description)
				messages.success(request, "New Blog Added")
				formData.save()
				form = BlogForm()
		else:
			form = BlogForm()
		return render(request, 'blog/addBlog.html', {'form' : form})
	else:
		return HttpResponseRedirect('/login')


def update_blog(request, id):
	if request.user.is_authenticated:
		if request.method == "POST":
			blogData = BlogPost.objects.get(pk=id)
			form = BlogForm(request.POST, instance=blogData)
			if form.is_valid():
				messages.success(request, "Blog Has Been Updated Successfully")
				form.save()
				return HttpResponseRedirect('/dashboard')
		else:
			blogData = BlogPost.objects.get(pk=id)
			form = BlogForm(instance=blogData)
		return render(request, 'blog/updateBlog.html', {'form' : form})
	else:
		return HttpResponseRedirect('/login')


def delete_blog(request, id):
	if request.user.is_authenticated:
		if request.method == "POST":
			blogData = BlogPost.objects.get(pk=id)
			blogData.delete()
			messages.success(request, "Blog Has Been Deleted Successfully")
		return HttpResponseRedirect('/dashboard')
	else:
		return HttpResponseRedirect('/login')

