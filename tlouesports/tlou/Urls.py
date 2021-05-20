from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('', views.defhome,name='home'),
    path('news', views.defnews),
    path('news/<str:title>', views.defsnews),
    path('games', views.defgames),
    path('ladders/<str:lname>', views.defladders),
    path('ladder/<str:lname>', views.defladder),
    path('signup', views.handleSignup),
    path('login', views.handleLogin),
    path('logout', views.handleLogout),
    path("validate/<str:user>", views.validate),
    path("profile/<str:user>", views.defprofile),
    path('contact', views.defcontact,name='contact'),
    path('update', views.user_update, name='update'),
    path('about/', views.aboutus, name='aboutus'),
    # path('contact/', views.contactus, name='contactus'),

    path('ranking/', views.ranking,),
    path('team-detail/<int:id>/', views.detail, ),

]
