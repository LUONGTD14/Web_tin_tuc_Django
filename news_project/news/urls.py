from os import name
from django.contrib import admin
from django.urls import path, include
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('category/<int:id>', category, name='category'),
    path('about/', about, name='about'),
    path('blog/', blog, name='blog'),
    path('blog_details/', blog_details, name='blog_details'),
    path('contact/', contact, name='contact'),
    path('elements/', elements, name='elements'),
    path('signin/', signin, name='signin'),
    path('sign-up/', sign_up, name='sign-up'),
    path('main/', my_Main, name='main'),
    path('feedback/', feedback, name='feedback'),
    path('search/', search, name='search'),
    path('post-details/<int:id>', post_details, name='post-details'),
    # path('sendMail/', sendMail, name='sendMail'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="sendMail.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="resetpassword\password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="resetpassword\password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="resetpassword\password_reset_done.html"), name="password_reset_complete"),
]
