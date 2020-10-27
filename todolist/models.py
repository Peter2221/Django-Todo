from django.db import models

# Create your models here.
class TodoItem(models.Model):
  todo_text = models.CharField(max_length=200)
  todo_status = models.BooleanField(default=False)
  pub_date = models.DateTimeField('date published')

  def __str__(self):
    return f"text: {self.todo_text}, done: {self.todo_status}, date: {self.pub_date}"