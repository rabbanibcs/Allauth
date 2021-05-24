
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from quickstart.views import UserViewSet,GroupViewSet
from view import views

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups',GroupViewSet)
router.register(r'student',views.StudentViewSet,basename='view')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls',namespace='rest_framework')),
    path('mixin/', include('snippets.urls')),
    path('generic/',include('generic.urls')),
    path('api/', include('api.urls')),
    # path('view',include('view.urls')),
]

