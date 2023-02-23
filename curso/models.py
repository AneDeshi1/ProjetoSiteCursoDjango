from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
LISTA_CATEGORIA = (
    ("PRGRAMACAO", "Programação"),
    ("DJANGO", "Django"),
    ("ingles", "Ingles"),
    ("desenho", "Desenho")
)

# Create your models here.


#criar o curso
class Curso(models.Model):
    thumb = models.ImageField(upload_to="Thumb_Cursos")
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    category = models.CharField(max_length=15, choices=LISTA_CATEGORIA)
    visualizacoes = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
#criar os episodios

class Episodio(models.Model):
    course = models.ForeignKey("Curso", related_name="episodios", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    video = models.URLField()

    def __str__(self):
        return self.filme.titulo + " - " + self.titulo

class Usuario(AbstractUser):
    cursos_vistos = models.ManyToManyField("Curso")

