from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Task(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    is_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        
        return reverse('task_detail', kwargs={'pk': self.pk})


class Subtask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='subtasks')
    title = models.CharField(max_length=200)
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} ({'done' if self.is_done else 'todo'})"

    def get_absolute_url(self):
        # Redirect to parent task detail view after subtask edit/delete
        return reverse('task_detail', kwargs={'pk': self.task.pk})
