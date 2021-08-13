from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import TodoItem

def todoView(request):
    all_items = TodoItem.objects.all()

    return render(request, 'todo.html', 
    {'all_items': all_items})

def addTodo(request):
    c = request.POST['content']
    new_item = TodoItem(content = c)
    new_item.save()
    return HttpResponseRedirect('/todo/')

def deleteTodo(request, todo_id):
    item_to_delete = TodoItem.objects.get(id = todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/todo/')
