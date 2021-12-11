from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework import permissions

from app.serializers import CommentSerializer
from .models import Comment


def hello(request):
    return HttpResponse("<h1>Hello, world!</h1>")

class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer