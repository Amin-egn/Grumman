from django.db import models
from django.contrib.auth.models import User

class TodoListModel(models.Model):
    """To-do List Model"""
    title = models.CharField(max_length=110)
    person = models.ForeignKey(User, related_name='lists', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class TodoItemModel(models.Model):
    """To-do Item Model"""
    title = models.CharField(max_length=110)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    status = models.CharField(max_length=20)
    owner = models.ForeignKey(User, related_name='owner', on_delete=models.DO_NOTHING)
    assign_to = models.ForeignKey(User, related_name='assign_to', on_delete=models.DO_NOTHING)
    todo_list = models.ForeignKey(TodoListModel, related_name='items', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['due_date']
