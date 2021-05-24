from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import StudentList, StudentDetail

urlpatterns = [
    path('list/', StudentList.as_view()),
    path('list/<int:pk>/', StudentDetail.as_view()),
]
# urlpatterns = format_suffix_patterns(urlpatterns)
