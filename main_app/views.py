from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib import messages

from .models import Task, Subtask
from .forms import TaskForm, SubtaskForm

def home(request):
    # landing page
    popular = None
    if request.user.is_authenticated:
        popular = Task.objects.filter(owner=request.user).order_by('-created_at')[:3]
    return render(request, 'home.html', {'popular': popular})

@login_required
def task_index(request):
    tasks = Task.objects.filter(owner=request.user)
    return render(request, 'task_index.html', {'tasks': tasks})

@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user
            task.save()
            messages.success(request, 'Task created.')
            return redirect(task.get_absolute_url())
    else:
        form = TaskForm()
    return render(request, 'task_form.html', {'form': form, 'is_create': True})

@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if task.owner != request.user:
        return HttpResponseForbidden()
    subtasks = task.subtasks.all()
    subtask_form = SubtaskForm()
    return render(request, 'task_detail.html', {
        'task': task,
        'subtasks': subtasks,
        'subtask_form': subtask_form
    })

@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if task.owner != request.user:
        return HttpResponseForbidden()
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated.')
            return redirect(task.get_absolute_url())
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_form.html', {'form': form, 'is_create': False, 'task': task})

@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if task.owner != request.user:
        return HttpResponseForbidden()
    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Task deleted.')
        return redirect('task-index')
    return render(request, 'task_confirm_delete.html', {'task': task})

# Subtask views
@login_required
def subtask_create(request, task_pk):
    task = get_object_or_404(Task, pk=task_pk)
    if task.owner != request.user:
        return HttpResponseForbidden()
    if request.method == 'POST':
        form = SubtaskForm(request.POST)
        if form.is_valid():
            sub = form.save(commit=False)
            sub.task = task
            sub.save()
            messages.success(request, 'Subtask added.')
            return redirect(task.get_absolute_url())
    return redirect('task-detail', pk=task_pk)

@login_required
def subtask_update(request, pk):
    sub = get_object_or_404(Subtask, pk=pk)
    if sub.task.owner != request.user:
        return HttpResponseForbidden()
    if request.method == 'POST':
        form = SubtaskForm(request.POST, instance=sub)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subtask updated.')
            return redirect(sub.task.get_absolute_url())
    else:
        form = SubtaskForm(instance=sub)
    return render(request, 'subtask_form.html', {'form': form, 'subtask': sub})

@login_required
def subtask_delete(request, pk):
    sub = get_object_or_404(Subtask, pk=pk)
    if sub.task.owner != request.user:
        return HttpResponseForbidden()
    if request.method == 'POST':
        task = sub.task
        sub.delete()
        messages.success(request, 'Subtask deleted.')
        return redirect(task.get_absolute_url())
    return render(request, 'subtask_confirm_delete.html', {'subtask': sub})

def about(request):
    return render(request, 'about.html')
