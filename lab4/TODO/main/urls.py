from django.urls import path
from main.views import *

urlpatterns = [
    path('todos/<int:list_id>/', todo_list),
    path('todos/<int:list_id>/completed/', completed_todo_list)
]
