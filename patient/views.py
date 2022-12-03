from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpRequest
from personnel.models import Personnel
from patient.models import Patient

# Create your views here.
def home(request):
  #  return HttpResponse('Bienvenue sur mon app DJANGO')
  all_patients =  Patient.objects.all()
  # Création de dictionnaire
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