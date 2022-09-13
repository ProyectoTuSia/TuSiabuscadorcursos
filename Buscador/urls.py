from django.urls import path
from .views import list_task, list_task2

urlpatterns = [
    path('', list_task),
    path('', list_task2)
]

