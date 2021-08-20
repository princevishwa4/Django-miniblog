from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="home"),
	path('about', views.about, name="about"),
	path('contact', views.contact, name="contact"),
	path('dashboard', views.dashboard, name="dashboard"),
	path('login', views.user_login, name="login"),
	path('register', views.user_register, name="register"),
	path('logout', views.user_logout, name="logout"),
	path('addBlog', views.add_blog, name="add_blog"),
	path('updateBlog/<int:id>', views.update_blog, name="update_blog"),
	path('deleteBlog/<int:id>', views.delete_blog, name="delete_blog"),
]