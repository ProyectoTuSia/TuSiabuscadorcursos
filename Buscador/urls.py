from django.urls import path
# from .views import list_task, list_task2
from . import views

urlpatterns = [
    # path('', list_task),
    # path('', list_task2),
    path('',views.filterCourses, name = 'filterCourses')
    
]

