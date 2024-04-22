from django.db import models
from django.contrib.auth.models import User



class Agent(models.Model):
    name = models.CharField(max_length=160)
    email = models.CharField(max_length=100,default='email')
    password = models.CharField(max_length=100)
    company_name = models.CharField(max_length=255)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name




class Buy(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    house_code = models.CharField(max_length=20)
    location = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    area = models.DecimalField(max_digits=10, decimal_places=2)
    image= models.ImageField(upload_to='images/',blank=True, null=True, default='images/default.jpg')



class Rent(models.Model):
    house_code = models.CharField(max_length=20)
    location = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    area = models.DecimalField(max_digits=10, decimal_places=2)
    image= models.ImageField(upload_to='images/',blank=True, null=True, default='images/default.jpg')

    def __str__(self):
        return self.house_code 


class Sell(models.Model):
    
    house_code = models.CharField(max_length=20)
    location = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    area = models.DecimalField(max_digits=10, decimal_places=2)
    image= models.ImageField(upload_to='images/',blank=True, null=True, default='images/default.jpg')
    
    def __str__(self):
        return self.house_code 

