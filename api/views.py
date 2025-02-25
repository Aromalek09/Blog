from django.shortcuts import render
from rest_framework import viewsets,generics
from rest_framework.viewsets import ModelViewSet,ViewSet
from rest_framework.serializers import Serializer
from .serializer import *
from .models import *
from .filters import *

# Create your views here.



class ProjectViewset(viewsets.ModelViewSet):
    queryset=Project.objects.all()
    serializer_class=ProjectSerializer
    filterset_class=ProjectFilter
    
    
class BlogView(generics.ListCreateAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer
    
class CommentsView(generics.ListCreateAPIView):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer