from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from main.views import TaskViewSet, CompletedViewSet, ListApiView

urlpatterns = [
    path('login', obtain_jwt_token),
    path('todos', ListApiView.as_view()),
    path('todos/<int:list_id>', TaskViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('todos/<int:list_id>/<int:task_id>', TaskViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('todos/<int:list_id>/completed/', CompletedViewSet.as_view({
        'get': 'list'
    }))
]
