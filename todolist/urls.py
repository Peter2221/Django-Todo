from django.urls import path
from . import views

app_name = 'todolist'
urlpatterns = [
  # /todos/
  path('', views.IndexView.as_view(), name="index"),
  # /todos/1/
  path('<int:todo_id>/', views.show_todo, name='show_todo'),
  # /todos/add/
  path('add/', views.add_todo, name="add_todo"),
  # /todos/delete/1
  path('delete/<int:todo_id>', views.delete_todo, name="delete_todo")
]