from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import ToDo

# Create your views here.
def index(request):
    return render(request, 'todos/index.html')

def list_todo_items(request):
    context = { 'todo_list': ToDo.objects.all().order_by('-id') }
    return render(request, 'todos/todo_list.html', context)

def insert_todo_item(request:HttpRequest):
    todo = ToDo(content = request.POST['content'])
    todo.save()
    return redirect('/todos/list/')

def update_selected_todo_status(request):
    if request.method == 'POST':
        for key in request.POST.keys():
            if key.startswith('status'):
                todo_id = int(key.split('_')[1])
                # print(key, todo_id, request.POST[key])
                if todo_id and request.POST[key]:
                    # print(todo_id, request.POST[key])
                    todo = ToDo.objects.get(id=todo_id)
                    todo.status = request.POST[key]
                    todo.save()
                    # print(todo.id, todo.content, todo.status)
    return redirect('/todos/list/')

def delete_todo_item(request, todo_id):
    todo_to_delete = ToDo.objects.get(id=todo_id)
    todo_to_delete.delete()
    return redirect('/todos/list/')