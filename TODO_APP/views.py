from django.shortcuts import render, redirect
from.models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')
    
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
        return redirect('list')
    return render(request, 'add_task.html')

def list(request):
    tasks = Task.objects.all()
    return render(request, 'add_list.html', {'tasks': tasks})
