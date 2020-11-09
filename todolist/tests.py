from django.test import TestCase
from django.http import HttpResponse
from django.urls import reverse
from django.utils import timezone

import datetime
from .models import TodoItem

# Create your tests here.
class TodoItemModelTests(TestCase):
  def test_was_published_recently_with_future_todo(self):
    """
    was_published_recently() returns False for todo whose pub_date
    is in the future 
    """
    time = timezone.now() + datetime.timedelta(days=30)
    future_todo = TodoItem(pub_date=time)
    self.assertIs(future_todo.was_published_recently(), False)

  def test_was_published_recently_with_old_todo(self):
    """
    was_published_recently() returns False for todo whose pub_date
    is older than 1 day
    """
    time = timezone.now() - datetime.timedelta(days=1, seconds=1)
    future_todo = TodoItem(pub_date=time)
    self.assertIs(future_todo.was_published_recently(), False)
    
  def test_was_published_recently_with_recent_todo(self):
    """
    was_published_recently() returns True for todo whose pub_date
    is recent, less or equal 1 day
    """
    time = timezone.now() - datetime.timedelta(days=1)
    future_todo = TodoItem(pub_date=time)
    self.assertIs(future_todo.was_published_recently(), True)
    
def create_todo(todo_text, days):
  """
  Create a todo with text and time, days > 0 for future,
  days < 0, for the past
  """
  time = timezone.now() + datetime.timedelta(days=days)
  return TodoItem.objects.create(todo_text=todo_text, pub_date=time)

class TodoIndexViewTests(TestCase):
  def test_no_todos(self):
    """
    If no todos exists appropriate message is shown
    """
    response = self.client.get(reverse('todolist:index'))
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, 'No todos available')
    self.assertQuerysetEqual(response.context['todo_items_list'], [])
  
  def test_future_question_past_question(self):
    """
    No matter of time created, both todos should be displayed
    """
    create_todo(todo_text="Future todo", days=30)
    create_todo(todo_text="Past todo", days=-30)
    response = self.client.get(reverse('todolist:index'))
    self.assertQuerysetEqual(
      response.context['todo_items_list'],
      ['<TodoItem: >']
    )

