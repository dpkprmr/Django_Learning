from django.urls import path

from . import views

urlpatterns = [
    path('', views.Courses, name='home-page'),
    path('<int:course_id>/', views.detail, name='details'),
]
