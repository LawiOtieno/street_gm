from django import forms
from django.shortcuts import render
from .forms import TodoForm
from .models import Todo


# Create your views here.

def index(request):
    return render(request, 'todo_app/index.html')

def create_todo(request):
    form = TodoForm()

    context={'form': form}

    if request.method=='POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        complete = request.POST.get('complete',False)

        todo=Todo()

        todo.title=title
        todo.description=description
        todo.complete=True if complete=="on" else False

        todo.save()

    return render(request, 'todo_app/create_todo.html', context)