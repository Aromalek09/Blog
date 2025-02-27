"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from api.views import *
from api.urls import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('comment',CommentsView .as_view(),name='comment'),
    path('blog',BlogView.as_view(),name='blog'),
    path('projects/', ProjectViewSet.as_view({'get': 'list'}), name='project-list'),        # List
    path('projects/create/', ProjectViewSet.as_view({'post': 'create'}), name='project-create'),  # Create a project
    path('projects/<int:pk>/', ProjectViewSet.as_view({'get': 'retrieve'}), name='project-detail'),  # Retrieve a single project
    path('projects/<int:pk>/update/', ProjectViewSet.as_view({'put': 'update'}), name='project-update'),  # Update a project
    path('projects/<int:pk>/delete/', ProjectViewSet.as_view({'delete': 'destroy'}), name='project-delete'),  # Delete a project
    
]
