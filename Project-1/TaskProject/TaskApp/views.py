from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Task

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages


# def index(request):
#     return HttpResponse("Hello, welcome to your Task Manager!")
#     return render(request, "TaskApp/index.html")




@login_required(login_url="/login/")
def index(request):

    if request.method == 'POST':
        task_name = request.POST.get('task')
        if task_name:
            Task.objects.create(name=task_name, user=request.user)
        return redirect('/')

    tasks = Task.objects.filter(user=request.user)
    return render(request, "TaskApp/index.html", {"tasks": tasks})


def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('/')



def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('/')




def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Registration failed. Try again.")
    else:
        form = UserCreationForm()
    return render(request, 'TaskApp/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Login failed. Check credentials.")
    else:
        form = AuthenticationForm()
    return render(request, 'TaskApp/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/login/')



