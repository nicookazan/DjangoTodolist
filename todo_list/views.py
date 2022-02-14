from django.shortcuts import render, get_object_or_404, redirect

from todo_list.forms import TaskForm
from todo_list.models import *

# Create your views here.
def bienvenido(request):
    tasks = Task.objects.order_by('id')
    if request.method == 'POST':
        formaTask = TaskForm(request.POST)
        if formaTask.is_valid():
            formaTask.save()
            return redirect('index')
    else:
        formaTask = TaskForm()
    return render(request, 'bienvenido-prueba.html', {'formaTask': formaTask, 'tasks': tasks})

def new(request):
    if request.method == 'POST':
        formaTask = TaskForm(request.POST)
        if formaTask.is_valid():
            formaTask.save()
            return redirect('index')
    else:
        formaTask = TaskForm()
    return render(request, 'new.html', {'formaTask':formaTask})

def edit(request, id):
    task = get_object_or_404(Task, pk=id)
    if request.method == 'POST':
        formaTask = TaskForm(request.POST, instance = task)
        if formaTask.is_valid():
            formaTask.save()
            return redirect('index')
    else:
        formaTask = TaskForm(instance=task)
    return render(request, 'edit.html', {'formaTask':formaTask})


def delete(request, id):
    task = get_object_or_404(Task, pk=id)
    if task:
        task.delete()
    return redirect('index')

def prueba(request):
    tasks = Task.objects.order_by('id')
    if request.method == 'POST':
        formaTask = TaskForm(request.POST)
        if formaTask.is_valid():
            formaTask.save()
            return redirect('index')
    else:
        formaTask = TaskForm()
    return render(request, 'bienvenido-prueba.html', {'formaTask':formaTask, 'tasks':tasks})