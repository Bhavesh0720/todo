from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_task', views.addTask, name='addTask'),
    path('mark_as_done/<int:pk>', views.markAsDone, name='markAsDone'),
    path('mark_as_undone/<int:pk>', views.markAsUnDone, name='markAsUnDone'),
    path('edit_task/<int:pk>', views.edit_task, name='edit_task'),
    path('delete_task/<int:pk>', views.delete_task, name='delete_task'),
]