from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from django.contrib.auth.models import User
from .forms import TaskForm

def index(request):
    if request.user.is_authenticated:
        tasks = Task.objects.filter(user=request.user)
        return render(request, 'index.html', {"tasks": tasks})
    else:
        return render(request, 'index.html', {"tasks": []})

def new_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user 
            task.save() 
            return redirect('index')
    else:
        form = TaskForm() 
        return render(request,'new_task.html',{'form':form})




def modify_task(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TaskForm(instance=task) 

    return render(request, 'modify_task.html', {'form': form, 'task': task})


def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('index') 

def completed_task(request,id):
    task=Task.objects.get(id=id)
    task.completed= not task.completed
    task.save()
    return redirect('index') 