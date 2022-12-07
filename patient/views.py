from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpRequest
from personnel.models import Personnel
from patient.models import Patient, Detail_patient
from personnel.models import Personnel

# Create your views here.
def home(request):
  #  return HttpResponse('Bienvenue sur mon app DJANGO')
  all_patients =  Patient.objects.all()
  # Création de dictionnaire
  patient_count = all_patients.count()
  context = {'patients':all_patients}
  return render(request, 'patient/index.html', context)

def add(request):
  return render(request,'patient/add_patient.html')

def save(request):
    if request.method == 'POST':
      prenom = request.POST['prenom']
      nom = request.POST['nom']
      age = request.POST['age']
      sexe = request.POST['sexe']
      telephone = request.POST['telephone']
      adress = request.POST['adresse']
      patient = Patient.objects.create(prenom=prenom, nom=nom, age=age, sexe=sexe, adresse=adress, telephone=telephone)
    return render(request, 'patient/add_patient.html')
def get_patient(request, id):
  patient = Patient.objects.get(pk=id)
  if not patient :
      all_intervention = []
  else :
      all_intervention = Detail_patient.objects.get(patient_id=id)
  return render(request, 'patient/dossier_patient.html', {'patient': patient, 'interventions': all_intervention})

def add_intervention(request, id):
  perso = Patient.objects.get(pk=id)
  all_personnels = Personnel.objects.all()
  return render(request, 'patient/add_intervention.html', {'personne': perso, 'personnels' : all_personnels})

def save_intervention(request):
  if request.method == 'POST':
    medecin = request.POST['medecin']
    paramedical = request.POST['paramedical']
    ambulancier = request.POST['ambulancier']
    motif_appel = request.POST['motif_appel']
    nom_appelant = request.POST['nom_appelant']
    telephone_appelant = request.POST['telephone_appelant']
    origine_appel = request.POST['origine_appel']
    lieu_intervention = request.POST['lieu_intervention']
    decision = request.POST['decision']
    trajet = request.POST['trajet']
    numero_ambulance = request.POST['num_ambulance']
    diagnostique = request.POST['diagnostique_evoque']
    patient = request.POST['id_patient']
    perso = Patient.objects.get(pk=request.POST['id_patient'])
    detail_patient = Detail_patient.objects.create(medecin=medecin,
                                                   paramedical=paramedical,
                                                   ambulancier=ambulancier,
                                                   Motif_appel=motif_appel,
                                                   nom_appelant=nom_appelant,
                                                   telephone_appelant=telephone_appelant,
                                                   origine_appel = origine_appel,
                                                   lieu_intervention = lieu_intervention,
                                                   decision = decision,
                                                   trajet = trajet,
                                                   numero_ambulance = numero_ambulance,
                                                   diagnostique_evoque = diagnostique,
                                                   patient_id = perso
                                                   )

    pat = {'patient': perso}
    return render(request, 'patient/dossier_patient.html', pat)