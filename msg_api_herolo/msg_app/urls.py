"""msg_api_herolo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, reverse
from .views import (
    MessageCreateView,
    MessageDeleteView,
    )
from . import views

app_name = 'msg_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('messages/compose/', views.compose, name='compose'),
    path('messages/unread/', views.unread, name='unread'),
    path('messages/<int:pk>/', views.show_msg, name='show_msg'),
    path('messages/<int:pk>/delete/', MessageDeleteView.as_view(), name='delete_msg'),
    path('messages/new/', MessageCreateView.as_view(), name='new_msg'),
]
