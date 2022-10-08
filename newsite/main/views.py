from django.shortcuts import render
from .models import Task


def index(request):
    tasks = Task.objects.all()
    context = {'title': 'Main page', 'task': tasks}
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def contacts(request):
    return render(request, 'contacts.html')
