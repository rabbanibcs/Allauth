from django.urls import path
from .views import StudentList,StudentDetail

urlpatterns=[

    path('list/',StudentList.as_view()),
    path('list/<int:pk>/', StudentDetail.as_view())
]