from django.db import models
from django.contrib.auth. models import User
from django . core .validators import MaxValueValidator , MinValueValidator

class Pet(models.Model):
    SPECIES_CHOICES= (
        ('dog','Dog'),  
        ('cat','Cat'),
        ('bird','Bird'),
        ('fish','Fish'),
        ('rabbit','Rabbit'),
    )
    species = models.CharField(max_length=10, choices=SPECIES_CHOICES, default='dog')
    id = models.AutoField(primary_key=True)  # custom primary key
    name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    image = models.CharField(max_length=2088)
    
    def __str__(self):
        return self.name
    
class Blog(models.Model):
    name = models.CharField(max_length=225)
    image =models.CharField(max_length=220)
    def __str__(self):
        return self.name
    
class Customer(models.Model):
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    name =models.CharField(max_length=220)
    city =models.CharField(max_length=50)
    number = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(9999999999)]
    )
    def __str__(self):
        return self.name
    
class Adoption(models.Model):
    status_options = (
        ('on_the_way','on the way'),
        ('arrived','arrived')
    )
    status = models.CharField(
        choices=status_options,
        default='on_the_way'
    )
    owned =models.ForeignKey(User,on_delete=models.CASCADE)
    pet =models.ForeignKey(Pet,on_delete=models.CASCADE)
    def __str__(self):
        return self.pet.name
    
class Donation(models.Model):
    user_name =models.ForeignKey(User,on_delete=models.CASCADE)
    donated = models.IntegerField()
    def __str__(self):
        return str(self.pk)
    # question ???
    
    
    



