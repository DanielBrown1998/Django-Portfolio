from django.db import models

# Create your models here.
class Project(models.Model):

    class Meta:
        ...

    CHOICES_TECNOLOGIES = {
    "images/django.svg": "DJANGO" ,
    "images/python.svg": "PYTHON",
    "images/dart.svg": "DART",
    "images/flutter.svg": "FLUTTER",
    }


    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(max_length=500, null=False, blank=False)
    link_github = models.URLField()
    tecnology = models.CharField(max_length=20, choices=CHOICES_TECNOLOGIES, blank=True, null=False, default="images/django.svg")
    image = models.ImageField(upload_to=f"images/", blank=True, null=True)

    def __str__(self):
        return self.name


class Advice(models.Model):

    name = models.CharField(max_length=50, blank=True, null=False, default="ANONIMOUS")
    text = models.TextField(max_length=500, blank=False, null=False)
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING)

    