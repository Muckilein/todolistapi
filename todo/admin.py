from django.contrib import admin
from .models import Todo

# Register your models here.

fields = ('text','chat','created_at','author', 'receiver')
list_display = ('created_at','chat','text','author', 'receiver')

admin.site.register(Todo)
