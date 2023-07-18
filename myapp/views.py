from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render
from .forms import newTaskForm, newProjectForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import newTaskForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, "index.html")


def signup(request):
    if request.method == "GET":
        return render(request, "auth/signup.html", {
            'form': UserCreationForm
        })
    else:
        if (request.POST["password1"] == request.POST["password2"]):
            username = request.POST["username"]
            password = request.POST["password1"]
            try:
                user = User.objects.create_user(
                    username=username, password=password)
                user.save()
                login(request, user)
                return redirect('dashboard')
            except IntegrityError:
                return render(request, "auth/signup.html", {
                    'form': UserCreationForm,
                    'error': "User already exists"
                })
        return render(request, "auth/signup.html", {
            'form': UserCreationForm,
            'error': "Passwords dont match"
        })


def signin(request):
    if request.method == "GET":
        return render(request, "auth/signin.html", {
            'form': AuthenticationForm
        })
    else:
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if (user is None):
            return render(request, "auth/signin.html", {
                'form': AuthenticationForm,
                'error': 'Username or password is incorrect'
            })
        else:
            login(request, user)
            return redirect('dashboard')


@login_required
def dashboard(request):
    return render(request, "dashboard.html")


@login_required
def signout(request):
    logout(request)
    return redirect('index')


@login_required
def projects(request):
    projects = Project.objects.all()
    return render(request, "projects/projects.html", {
        "projects": projects
    })


@login_required
def project(request, id):
    project = get_object_or_404(Project, pk=id)
    tasks = Task.objects.filter(project_id=id)
    return render(request, "projects/project.html", {
        "project": project,
        "tasks": tasks
    })


@login_required
def task_detail(request, id):
    task = get_object_or_404(Task, pk=id, user=request.user)
    if (request.method == "GET"):
        form = newTaskForm(instance=task)
        return render(request, "tasks/task.html", {
            "task": task,
            "form": form
        })
    else:
        try:
            form = newTaskForm(request.POST, instance=task)
            form.save()
            return redirect('tasks')
        except ValueError:
            return render(request, "tasks/task.html", {
                "task": task,
                "form": form,
                "error": "Error updating task"
            })


@login_required
def complete_task(request, id):
    task = get_object_or_404(Task, pk=id, user=request.user)
    if (request.method == "POST"):
        task.date_completed = timezone.now()
        task.save()
        return redirect('tasks')


@login_required
def delete_task(request, id):
    task = get_object_or_404(Task, pk=id, user=request.user)
    if (request.method == "POST"):
        task.delete()
        return redirect('tasks')


@login_required
def tasks(request):
    tasks = Task.objects.filter(user=request.user, date_completed__isnull=True)
    return render(request, "tasks/tasks.html", {
        "tasks": tasks
    })


@login_required
def completed_tasks(request):
    tasks = Task.objects.filter(
        user=request.user, date_completed__isnull=False).order_by('-date_completed')
    return render(request, "tasks/tasks.html", {
        "tasks": tasks
    })


@login_required
def newProject(request):
    if request.method == "GET":
        return render(request, "projects/newProject.html", {
            "form": newProjectForm()
        })
    else:
        name = request.POST["name"]
        Project.objects.create(name=name)
        return redirect("projects")


@login_required
def newTask(request):
    if request.method == "GET":
        return render(request, "tasks/newTask.html", {
            "form": newTaskForm()
        })
    else:
        try:
            title = request.POST["title"]
            description = request.POST["description"]
            project = request.POST["project"]
            Task.objects.create(title=title,
                                description=description, project_id=project, user=request.user)
            return redirect("tasks")
        except ValueError:
            return render(request, "tasks/newTask.html", {
                "form": newTaskForm(),
                "error": "Please provide valid data"
            })
