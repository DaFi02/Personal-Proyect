from django.db import models

# Create your models here.
from django.db import models
from apps.accounts.models import Account


class Proyect(models.Model):
    CATEGORY_PROYECTS = [
        ("WO", "Work"),
        ("ST", "Study"),
        ("LI", "Life"),
    ]
    #TODO: add field for image
    name_proyect = models.CharField("name for the proyect", max_length=50)
    description = models.CharField(max_length=200)
    category_proyects = models.CharField(max_length=2, choices=CATEGORY_PROYECTS, default="LI")
    account = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['name_proyect']
        verbose_name = 'Proyect'
        verbose_name_plural = 'Proyects'

    def __str__(self):
        return self.name_proyect


class Task(models.Model):
    STATUS_TASK = [
        ("DO", "Done"),
        ("PE", "Pending"),
        ("IN", "In progress"),
    ]

    Title = models.CharField("name for the task", max_length=50)
    description = models.CharField(max_length=200)
    proyect = models.ForeignKey(Proyect, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    status_task = models.CharField(max_length=2, choices=STATUS_TASK, default="PE")

    class Meta:
        ordering = ['date']
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return self.Title

# python manage.py make migrations => generate code for change in Db  (create table)
# python manage.py migrate
