from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Task

# Create your views here.
def home(request):
    tasks = Task.objects.filter(is_completed=False)
    completed_tasks = Task.objects.filter(is_completed=True)
    con = {
        'tasks':tasks,
        'completed_tasks':completed_tasks,
    }
    return render(request, 'home.html', con)


def addTask(request):
    if request.method=='POST':
        task = request.POST['task']
        Task.objects.create(task=task)
    return redirect('home')
