
from django.contrib import admin
from django.urls import path
from request.views import request

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',request,name='request' ),


]
