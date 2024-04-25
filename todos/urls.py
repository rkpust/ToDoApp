from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.list_todo_items),
    path('insert_todo/', views.insert_todo_item),
    path('update_todos_status/', views.update_selected_todo_status, name='update_selected_todo_status'),
    path('delete_todo/<int:todo_id>/', views.delete_todo_item, name='delete_todo_item')
]