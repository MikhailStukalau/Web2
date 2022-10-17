from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.all()
    context = {'title': 'Main page', 'task': tasks}
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def contacts(request):
    return render(request, 'contacts.html')

# def create(request):
#     form = TaskForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'create.html')

def task_detail(request, pk):
    tasks = Task.objects.get(pk=pk)
    context = {
        'tasks': tasks
    }
    return render(request, 'task_detail.html', context)

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = form.save()
            return redirect('home')
    else:
        form = TaskForm()
    return render(request, 'create.html', {'form': form})

