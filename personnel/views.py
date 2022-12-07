from curses.ascii import HT
from django.shortcuts import render
from personnel.models import Personnel

def liste(request):
    all_personnel = Personnel.objects.all()
    # Création de dictionnaire
    patient_count = all_personnel.count()
    context = {'personnel_liste': all_personnel}
    return render(request, 'personnel/index.html', context)

def add(request):
    return render(request, 'personnel/add_personnel.html')

def save(request):
    if request.method == 'POST':
      matricule = request.POST['matricule']
      prenom = request.POST['prenom']
      nom = request.POST['nom']
      tel = request.POST['telephone']
      adress = request.POST['adresse']
      profile = request.POST['profil']
      specialite = request.POST['specialite']
      personnel = Personnel.objects.create(matricule=matricule,prenom_personnel=prenom, nom_personnel=nom,profile=profile,specialite=specialite, adresse_personnel=adress, telephone_personnel=tel)
    return render(request, 'personnel/add_personnel.html')