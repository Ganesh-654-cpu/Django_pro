# from django.db import models

# # Create your models here.

# class reg(models.Model):
#     name=models.CharField(max_length=100)
#     email=models.EmailField()
#     password=models.CharField(max_length=100)
#     contact=models.CharField(max_length=15)
#     address=models.CharField(max_length=200, default='pune')
#     city=models.CharField(max_length=100, default='mumbai')
    
#     def __str__(self):
#         return self.name

    
    
#     class employee(models.Model):
#         email=models.CharField(max_length=100)
#         photo=models.FileField(upload_to='files')
    
#     def __str__(self):
#         return self.email
    
from django.db import models

class reg(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    address = models.CharField(max_length=200, default='pune')
    city = models.CharField(max_length=100, default='mumbai')

    def __str__(self):
        return self.name


class employee(models.Model):
    email = models.CharField(max_length=100)
    photo = models.FileField(upload_to='images')

    def __str__(self):
        return self.email
    
    
class person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    address = models.CharField(max_length=200, default='pune')
    city = models.CharField(max_length=100, default='mumbai')

    def __str__(self):
        return self.name
    
    

