from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
		path('',views.Home,name='home'),
		path('register/',views.register,name='register'),
		path('login/', auth_views.LoginView.as_view(template_name='appoint/login.html'), name='login'),
		path('logout/', auth_views.LogoutView.as_view(template_name='appoint/logout.html'), name='logout'),
		path('appointment/',views.Form,name='form'),

]