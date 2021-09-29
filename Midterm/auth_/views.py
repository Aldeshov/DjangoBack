from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from auth_.models import CustomUser


class UserViewSet(viewsets.ViewSet):
    def create(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")

        CustomUser.objects.create_user(username, password)
        return Response({"message": "Created"})
