from django.db import models


# Create your models here.
from professores.models import Professor


class Aluno(models.Model):
    nome = models.CharField(
        max_length=255,

    )
    idade = models.IntegerField()
    email = models.EmailField()
    prof_favorito = models.ForeignKey(
        Professor,
        on_delete=models.CASCADE,
        related_name='alunos_professor'
    )



