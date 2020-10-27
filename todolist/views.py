from django.shortcuts import redirect, render
from django.http import HttpResponse, Http404
from django.template import loader
from django.utils import timezone

from .models import TodoItem

def index(request):
    try:
        todo_items_list = TodoItem.objects.order_by('-pub_date')
    except TodoItem.DoesNotExist:
        raise Http404("Todo does not exist")
    return render(request, 'todolist/index.html', {'todo_items_list' : todo_items_list})

def add_todo(request):
    if(request.method == 'POST'):
        todo_text = request.POST['todo_text']
        date = timezone.now()
        todo = TodoItem(todo_text=todo_text, pub_date=date)
        todo.save()

        return redirect('/todos')
    else:
        return render(request, 'todolist/add.html')

def show_todo(request, todo_id):
    try:
        todo = TodoItem.objects.get(pk=todo_id)
    except TodoItem.DoesNotExist:
        raise Http404("Todo does not exist")
    return render(request, 'todolist/details.html', {'todo' : todo})

