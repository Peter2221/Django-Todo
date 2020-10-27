from django.urls import path
from . import views

urlpatterns = [
  # /todos/
  path('', views.index, name="index"),
  # /todos/1/
  path('<int:todo_id>/', views.show_todo, name='show_todo'),
  # /todos/add/
  path('add/', views.add_todo, name="add_todo")
]