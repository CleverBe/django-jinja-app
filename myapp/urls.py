from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.signin, name="login"),
    path('logout/', views.signout, name="logout"),
    path('projects/', views.projects, name="projects"),
    path('projects/<str:id>', views.project, name="project"),
    path('newProject/', views.newProject, name="newProject"),
    path('tasks/', views.tasks, name="tasks"),
    path('tasks_completed/', views.completed_tasks, name="tasks_completed"),
    path('tasks/<str:id>', views.task_detail, name="task"),
    path('tasks/<str:id>/complete', views.complete_task, name="complete_task"),
    path('tasks/<str:id>/delete', views.delete_task, name="delete_task"),
    path('newTask/', views.newTask, name="newTask"),
]
