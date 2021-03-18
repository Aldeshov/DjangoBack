from django.urls import path
from main.views import *

urlpatterns = [
    path('todos/', todo_list),
    path('todos/1/completed/', completed_todo_list)
]
