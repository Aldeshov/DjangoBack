from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status

from main.models import Book, Journal
from main.serializers import BookSerializer, JournalSerializer
from utils.roles import *


class BookViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)

    def get_access(self, user):
        if user.role == Guest:
            return False
        else:
            return True

    def list(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def retrieve(self, request, book_id):
        book = Book.objects.get(id=book_id)
        serializer = BookSerializer(book, many=False)
        return Response(serializer.data)

    def create(self, request):
        if self.get_access(request.user):
            book = Book.objects.create(name=request.data.get("name"),
                                       price=request.data.get("price"),
                                       description=request.data.get("description"),
                                       created_at=request.data.get("created_at"),
                                       num_pages=request.data.get("num_pages"),
                                       genre=request.data.get("genre"))
            book.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, book_id):
        if self.get_access(request.user):
            book = Book.objects.get(id=book_id)
            book.name = request.data.get("name"),
            book.price = request.data.get("price"),
            book.description = request.data.get("description"),
            book.created_at = request.data.get("created_at"),
            book.num_pages = request.data.get("num_pages"),
            book.genre = request.data.get("genre")
            book.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, book_id):
        if self.get_access(request.user):
            try:
                book = Book.objects.get(id=book_id)
                book.delete()
                return Response(status=status.HTTP_200_OK)
            except Book.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class JournalViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)

    def get_access(self, user):
        if user.role == Guest:
            return False
        else:
            return True

    def list(self, request):
        journals = Journal.objects.all()
        serializer = JournalSerializer(journals, many=True)
        return Response(serializer.data)

    def retrieve(self, request, journal_id):
        journal = Journal.objects.get(id=journal_id)
        serializer = JournalSerializer(journal, many=False)
        return Response(serializer.data)

    def create(self, request):
        if self.get_access(request.user):
            journal = Journal.objects.create(name=request.data.get("name"),
                                             price=request.data.get("price"),
                                             description=request.data.get("description"),
                                             created_at=request.data.get("created_at"),
                                             type=request.data.get("type"),
                                             publisher=request.data.get("publisher"))
            journal.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, journal_id):
        if self.get_access(request.user):
            journal = Journal.objects.get(id=journal_id)
            journal.name = request.data.get("name"),
            journal.price = request.data.get("price"),
            journal.description = request.data.get("description"),
            journal.created_at = request.data.get("created_at"),
            journal.type = request.data.get("type"),
            journal.publisher = request.data.get("publisher")
            journal.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, journal_id):
        if self.get_access(request.user):
            try:
                journal = Journal.objects.get(id=journal_id)
                journal.delete()
                return Response(status=status.HTTP_200_OK)
            except Journal.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
