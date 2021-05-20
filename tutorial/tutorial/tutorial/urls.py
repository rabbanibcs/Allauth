
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from quickstart.views import UserViewSets,GroupViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSets)
router.register(r'groups',GroupViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',namespace='rest_framework')),

]
