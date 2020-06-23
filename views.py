from django.shortcuts import render
from .models import ToDoItems
from django.http import HttpResponseRedirect


# Create your views here.
def todoViews(request):
    all_items = ToDoItems.objects.all()
    return render(request,'todo_app/index.html',
                  {'all_item':all_items})
def addTodo(request):
    new_item = ToDoItems(content = request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todo/')
def deleteTodo(request,todo_id):
    d_item = ToDoItems.objects.get(id=todo_id)
    d_item.delete()
    return HttpResponseRedirect('/todo/')