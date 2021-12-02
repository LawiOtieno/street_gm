from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'todo_app/index.html')

def create_todo(request):
    return render(request, 'todo_app/create_todo.html')