
from email import message
from pickletools import read_uint1
from django.shortcuts import HttpResponse, redirect, render
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib import messages


import tasks
from .models import Task
from .forms import AddTaskForm, DetailTaskForm, UpdateTaskForm, CreateTaskForm
# Create your views here.



def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)

def homePage(request):
    return render(request, 'tasks/home.html')

def todoList(request):
    # form = AddTaskForm() 
     
    profile = request.user.profile  
    tasks = Task.objects.filter(owner=profile)

    search_query = request.GET.get('text')
    if search_query:
        response = Task.objects.filter(name__icontains=search_query, owner=profile)

        tasks = response

    incomplete = tasks.filter(completed=False).count()
    context = {'tasks': tasks, 'incomplete': incomplete, 'search_query': search_query }
    return render(request, 'tasks/todo.html', context)

def todoDetail(request, pk):
    form = DetailTaskForm()
    task = Task.objects.get(id=pk)
    context = {'task': task, 'form': form}
    return render(request, 'tasks/todo_detail.html', context)

def todoUpdate(request, pk):
    task = Task.objects.get(id=pk)
    form = UpdateTaskForm(instance=task) 
    
    if request.method == "POST":
        form = UpdateTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'The task was successfully updated.')
            return redirect('tasks')
               
    context = {'task': task, 'form': form}
    return render(request, 'tasks/todo_form.html', context)

def todoCreate(request):
    page = 'create'
    form = CreateTaskForm()

    if request.method == 'POST':
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user.profile
            task.save()
            messages.success(request, 'The task was successfully created.')
            return redirect('tasks')
    context = {'form': form, 'page': page}
    return render(request, 'tasks/todo_form.html', context)      

def todoDelete(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == 'POST':
        task.delete()
        messages.success(request, 'The task was successfully deleted.')
        
        return redirect('tasks')
    context = {'task': task}
    return render(request, 'tasks/delete_form.html', context)


def todoComplete(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        task = Task.objects.get(id=pk)
        task.completed = True
        task.save()
        messages.success(request, 'The task was successfully completed.')

        return redirect('tasks')
    context = {'task': task}    
    return render(request, 'tasks/todo_complete.html', context)        



