from django.http import HttpResponse
from django.shortcuts import render
from main.models import *


def data(list_id):
    try:
        current_list = List.objects.get(id=list_id)
    except List.DoesNotExist:
        return {}
    tasks = Task.objects.filter(list=current_list)

    context = {
        "list": current_list,
        "tasks": tasks
    }
    return context


def todo_list(request, list_id):
    get = data(list_id)
    if get == {}:
        return HttpResponse("Not Found")
    return render(request, 'todo_list.html', context=get)


def completed_todo_list(request, list_id):
    get = data(list_id)
    if get == {}:
        return HttpResponse("Not Found")
    return render(request, 'completed_todo_list.html', context=get)
