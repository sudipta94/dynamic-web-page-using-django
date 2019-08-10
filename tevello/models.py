from django.db import models

# Create your models here.
class destination(models.Model):
    place=models.CharField(max_length=100)
    image=models.ImageField(upload_to='pics')
    des=models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField(default=False)
class post(models.Model):
    date=models.IntegerField()
    month=models.CharField(max_length=10)
    title=models.CharField(max_length=50)
    tag=models.CharField(max_length=50)
    des=models.TextField()
    image=models.ImageField(upload_to='post')