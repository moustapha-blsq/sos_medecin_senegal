from django.db import models

"""
class Tag(models.Model):
   nom = models.CharField(max_length=100, null= True)
    def __str__(self):
        return self.nom"""

class Patient(models.Model):
    prenom = models.CharField(max_length=200)
    nom    = models.CharField(max_length=100)
    age    = models.IntegerField(null=True)
    sexe   = models.CharField(max_length=5)
    adresse = models.CharField(max_length=500)
    telephone = models.CharField(max_length=50)
    date_creation = models.DateTimeField(auto_now_add=True, null=True)
    class Meta:
        db_table = 'patient'