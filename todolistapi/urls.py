from rest_framework import routers
from django.urls import include, path
from django.contrib import admin
from todo.views import TodoViewSet

router = routers.DefaultRouter()
router.register(r'todos', TodoViewSet)

urlpatterns = [   
    path('', include(router.urls)),
    path('admin/', admin.site.urls)   
]
