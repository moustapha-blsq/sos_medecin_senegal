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

class Horaire(models.Model):
    libelle = models.CharField(max_length=100)
    heure = models.CharField(max_length=25)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    class Meta:
        db_table = 'horaire'

class Lesions(models.Model):
    libelle_lesion = models.CharField(max_length=100)
    class Meta:
        db_table = 'lesion'
class Organe(models.Model):
    nom_organe = models.CharField(max_length=100)
    class Meta:
        db_table = 'organe'
class Diagnostique_lesion_organe(models.Model):
    resultat_diagnostique = models.CharField(max_length=100)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    lesion_id = models.ForeignKey(Lesions, on_delete=models.CASCADE)
    organe_id = models.ForeignKey(Organe, on_delete=models.CASCADE)
    class Meta:
        db_table = 'diagnostique_lesion_organe'
class Detail_patient(models.Model):
    medecin = models.CharField(max_length=150, null=True)
    paramedical = models.CharField(max_length=150, null=True)
    ambulancier = models.CharField(max_length=150, null=True)
    origine_appel = models.CharField(max_length=100)
    Motif_appel = models.CharField(max_length=150)
    nom_appelant = models.CharField(max_length=150)
    telephone_appelant = models.CharField(max_length=50)
    lieu_intervention = models.CharField(max_length=100)
    decision = models.CharField(max_length=100)
    trajet = models.CharField(max_length=200)
    numero_ambulance = models.CharField(max_length=20)
    diagnostique_evoque = models.CharField(max_length=250)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    class Meta:
        db_table = 'detail_patient'

class Signe_de_vie(models.Model):
    libelle_signe = models.CharField(max_length=150)
    description = models.CharField(max_length=100, null=True)
    class Meta:
        db_table = 'signe_de_vie'

class Rubrique_signe_de_vie(models.Model):
    nom_rubrique = models.CharField(max_length=100, null=True)
    class Meta:
        db_table = 'rubrique_signe_de_vie'
class Score_signe_de_vie(models.Model):
    score = models.IntegerField(null=True)
    signe_vie_id = models.ForeignKey(Signe_de_vie, on_delete=models.CASCADE)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    rubrique_signe_vie_id = models.ForeignKey(Rubrique_signe_de_vie, on_delete=models.CASCADE)
    class Meta:
        db_table = 'score_signe_de_vie'

class Autre_indice_signe_vie(models.Model):
    fourmillement_extremites = models.CharField(max_length=10)
    mouvement_des_ms = models.CharField(max_length=10)
    mouvement_des_mi = models.CharField(max_length=10)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    class Meta:
        db_table = 'autres_indice_signe_vie'

class traitement_primaire(models.Model):
    mise_en_condition = models.CharField(max_length=50)
    solute_drogue = models.CharField(max_length=200)
    voie_aerienne = models.CharField(max_length=100)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    class Meta:
        db_table = 'traitement_primaire'
class consultation(models.Model):
    element_consulte = models.CharField(max_length=100)
    heure = models.CharField(max_length=20)
    resultat = models.CharField(max_length=50)
    commentaire = models.CharField(max_length=150)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    class Meta:
        db_table = 'consultation'

class Origine(models.Model):
    pays_origine = models.CharField(max_length=20)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    class Meta:
        db_table = 'origine'

class Consommable(models.Model):
    libelle_consommable = models.CharField(max_length=100)
    class Meta:
        db_table = 'consommables'

class Consommable_utilise(models.Model):
    libelle_consommable_utilise = models.CharField(max_length=100)
    nombre = models.IntegerField(null=True)
    charges = models.CharField(max_length=100)
    fnc = models.CharField(max_length=100)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    class Meta:
        db_table = 'consommables_utilises'