instalar python o python3

instalar pip

pip install virtualenv

virtualenv --version

sudo apt-get install python3-virtualenv

virtualenv venv

F1 - select interpreter - seleccionar python venv

pip install django

django-admin --version

django-admin startproject mysite .

python manage.py runserver
python manage.py runserver 3000

python manage.py --help

python manage.py startapp myapp

python manage.py makemigrations

python manage.py migrate

python manage.py shell
from myapp.models import Project, Task
p=Project(name="nuevo proyecto")
p.save()
Project.objects.all()
p=Project.objects.get(id=1)
p.task_set.all()
p.task_set.create(title="probar ide",description="desarrollar")
p.task_set.get(id=1)
Project.objects.filter(name__startswith="aplication")

python manage.py createsuperuser

clever
clever123

borrar migraciones y db.sqlite3


