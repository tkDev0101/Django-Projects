from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Task


# def index(request):
#     return HttpResponse("Hello, welcome to your Task Manager!")
#     return render(request, "TaskApp/index.html")


def index(request):

    if request.method == 'POST':
        task_name = request.POST.get('task')
        if task_name:
            Task.objects.create(name=task_name)
        return redirect('/')

    tasks = Task.objects.all()
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



