from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_task', views.addTask, name='addTask'),
    path('mark_as_done/<int:pk>', views.markAsDone, name='markAsDone'),
]