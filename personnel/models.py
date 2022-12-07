from django.db import models

class Personnel (models.Model):
    """PERSONNEL_PROFIL_CHOICES = (
        ('médecin', 'Médecin'),
        ('paramédical', 'Paramédical'),
        ('ambulancier', 'Ambulancier')
    )"""
    matricule=models.CharField(max_length=25)
    prenom_personnel = models.CharField(max_length=200)
    nom_personnel = models.CharField(max_length=200)
    telephone_personnel=models.CharField(max_length=25, null=True)
    adresse_personnel = models.CharField(max_length=500, null=True)
    profile = models.CharField(max_length=50)
    specialite = models.CharField(max_length=250, null=True)
    date_creation=models.DateTimeField(auto_now_add=True, null=True)
    class Meta:
        db_table = 'personnel'
    def __str__(self):
        return self.nom_personnel