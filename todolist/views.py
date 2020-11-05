from django.shortcuts import redirect, render
from django.http import HttpResponse, Http404
from django.template import loader
from django.utils import timezone
from django.views import generic

from .models import TodoItem

class IndexView(generic.ListView):
    template_name = 'todolist/index.html'
    context_object_name = 'todo_items_list'

    def get_queryset(self):
        return TodoItem.objects.order_by('-pub_date')

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

