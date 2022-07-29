from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('tasks/', views.todoList, name='tasks'),
    path('todo-detail/<str:pk>/', views.todoDetail, name='todo-detail'),
    path('todo-update/<str:pk>/', views.todoUpdate, name='todo-update'),
    path('todo-create/', views.todoCreate, name='todo-create'),
    path('todo-delete/<str:pk>/', views.todoDelete, name='todo-delete'),
    path('todo-complete/<str:pk>/', views.todoComplete, name='todo-complete'),
    
]

handler404 = 'tasks.views.page_not_found_view'