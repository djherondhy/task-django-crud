from django.db import models

class Tarefa(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=255)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'Descrição: {self.descricao }| Status: {self.status}'