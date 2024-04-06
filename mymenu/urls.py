from django.urls import path
from .views import index, hello, world

urlpatterns = [
    path('', index, name='index'),
    path('hello', hello, name='hello'),
    path('world/<int:pk>', world, name='world'),
]
