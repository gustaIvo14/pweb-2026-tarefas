from django.db import models

class Tarefa(models.Model):
    nome = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    prazo = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nome