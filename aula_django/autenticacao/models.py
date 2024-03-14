from django.db import models
from django.db.models.fields import CharField, EmailField


class Pessoa(models.Model):
    nome = CharField(max_length=100)
    email = EmailField()
    senha = CharField(max_length=100)



# How to make Django recreate the deleted table?
    
# 1. Delete your migrations folder
# 2. In the database: DELETE FROM django_migrations WHERE app = 'app_name'.
#    You could alternatively just truncate this table.
# 3. python manage.py makemigrations app_name
# 4. python manage.py migrate