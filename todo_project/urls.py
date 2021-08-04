"""todo_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('completed', views.get_completed, name='get_completed'),
    path('unfinished', views.get_unfinished, name='get_unfinished'),
    path('add', views.add, name='add'),
    path('edit/<int:identifier>', views.edit, name='edit'),
    path('delete/<int:identifier>', views.delete, name='delete'),
    path('complete/<int:identifier>', views.complete, name='complete'),
    path('remove_complete/<int:identifier>', views.remove_complete, name='remove_complete')
]
