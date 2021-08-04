from django.contrib import admin
from .models import Task
from django.db import models
from django import forms

# Register your models here.

admin.site.register(Task)   # register task model with admin