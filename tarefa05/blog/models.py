from django.db import models

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to="posts")
    data = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.titulo