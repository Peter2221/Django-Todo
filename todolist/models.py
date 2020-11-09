from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class TodoItem(models.Model):
  todo_text = models.CharField(max_length=200)
  todo_status = models.BooleanField(default=False)
  pub_date = models.DateTimeField('date published')

  def was_published_recently(self):
    now = timezone.now()
    return now - datetime.timedelta(days=1) <= self.pub_date <= now

  def __str__(self):
    return f"{self.todo_text}"