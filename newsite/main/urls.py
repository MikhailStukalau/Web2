from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('add_task/', views.add_task, name='add_task'),
    path('<int:pk>/', views.task_detail, name='task_detail')
]