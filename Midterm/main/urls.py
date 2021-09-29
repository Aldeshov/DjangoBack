from django.urls import path, include

from main.views import BookViewSet, JournalViewSet

urlpatterns = [
    path('books', BookViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('journals', JournalViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('books/<int:book_id>', BookViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('journals/<int:journal_id>', JournalViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    }))
]
