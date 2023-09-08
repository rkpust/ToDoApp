from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import ToDo

# Create your views here.

def list_todo_items(request):
    context = { 'todo_list': ToDo.objects.all() }
    return render(request, 'todos/todo_list.html', context)

def insert_todo_item(request:HttpRequest):
    todo = ToDo(content = request.POST['content'])
    todo.save()
    return redirect('/todos/list/')