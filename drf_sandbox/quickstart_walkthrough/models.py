from django.db import models

# Create your models here.
class Cat(models.Model):
    Name = models.CharField(max_length=100)
    Age = models.IntegerField()
    FavFood = models.CharField()

    def __str__(self) -> str:
        return self.Name
    
    class Meta:
        ordering = ['-id']