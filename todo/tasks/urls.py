from django.urls import path
from . import views

urlpatterns = [
    path('helloword/', views.helloWordId),
    path('', views.taskList, name='task-list'),
    path('task/<int:id>', views.taskView, name="task-view"),
    path('newTask/', views.newTask, name='new-Task'),
    path('edit/<int:id>', views.editTask, name='edit-task'),
    path('delete/<int:id>', views.deleteTask, name='delete-task'),
    path('yourname/<str:name>', views.yourName, name='your-name'),
]
