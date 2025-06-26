from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Task

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

from django.http import HttpResponseForbidden

# def index(request):
#     return HttpResponse("Hello, welcome to your Task Manager!")
#     return render(request, "TaskApp/index.html")



@login_required(login_url="/login/")
def index(request):
    if request.method == 'POST':
        task_name = request.POST.get('task')
        due_date = request.POST.get('due_date') or None
        priority = request.POST.get('priority') or 'Medium'

        if task_name:
            Task.objects.create(
                name=task_name,
                user=request.user,
                due_date=due_date,
                priority=priority
            )
        return redirect('/')

    tasks = Task.objects.filter(user=request.user).order_by('completed', 'due_date')
    return render(request, "TaskApp/index.html", {"tasks": tasks})




@login_required(login_url="/login/")
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    # Ensure users can only edit their own tasks
    if task.user != request.user:
        return HttpResponseForbidden("You are not allowed to edit this task.")

    if request.method == 'POST':
        new_name = request.POST.get('name')
        if new_name:
            task.name = new_name
            task.save()
            return redirect('/')
    
    return render(request, 'TaskApp/edit.html', {'task': task})




def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('/')



def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('/')




# ------------------ Login / Register / Logout ------------------ #

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



