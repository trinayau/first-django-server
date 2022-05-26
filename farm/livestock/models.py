from django.db import models

# Create your models here.
# Inheritance - classes inherit from other classes
# There is a model that we pull from
# Create model for our db, models.Model is boilerplate, Django knows how to deal w it
class Species(models.Model):
    name = models.CharField(max_length=100)

    def __repr__(self):
        return "Species: " + self.name
    
    def __str__(self):
        return "Species: " + self.name

class Animal(models.Model):
    name = models.CharField(max_length=15)
    species = models.ForeignKey(Species,
                                on_delete=models.SET_NULL,
                                null=True)
    age = models.IntegerField()
    hopes_and_dreams = models.CharField(max_length=1000)

    def __repr__(self):
        return f"{self.name}, a {self.species.name}"
    
    def __str__(self):
        return f"{self.name}, a {self.species.name}"
    
    def to_dict(self):
        return {
            "name": self.name,
            "species": self.species.name,
            "age": self.age,
            "hopes_and_dreams": self.hopes_and_dreams
        }



