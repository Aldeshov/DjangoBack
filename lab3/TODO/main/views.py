from django.shortcuts import render
import json


def todo_list(request):
    with open('tasks.json') as f:
        tasks = json.load(f)
    context = {
        "data": tasks
    }
    return render(request, 'todo_list.html', context=context)


def completed_todo_list(request):
    with open('tasks.json') as f:
        tasks = json.load(f)
    context = {
        "data": tasks
    }
    return render(request, 'completed_todo_list.html', context=context)
