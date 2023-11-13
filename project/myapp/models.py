from django.db import models

# Create your models here.
class employee(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    address=models.TextField()
    phone=models.IntegerField()



