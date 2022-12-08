from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpRequest
from personnel.models import Personnel
from patient.models import Patient, Detail_patient, Horaire, Lesions, Diagnostique_lesion_organe, Signe_de_vie, Rubrique_signe_de_vie
from personnel.models import Personnel


# Create your views here.
def home(request):
    #  return HttpResponse('Bienvenue sur mon app DJANGO')
    all_patients = Patient.objects.all()
    # Création de dictionnaire
    patient_count = all_patients.count()
    context = {'patients': all_patients}
    return render(request, 'patient/index.html', context)


def add(request):
    return render(request, 'patient/add_patient.html')


def save(request):
    if request.method == 'POST':
        prenom = request.POST['prenom']
        nom = request.POST['nom']
        age = request.POST['age']
        sexe = request.POST['sexe']
        telephone = request.POST['telephone']
        adress = request.POST['adresse']
        patient = Patient.objects.create(prenom=prenom, nom=nom, age=age, sexe=sexe, adresse=adress,
                                         telephone=telephone)
    return render(request, 'patient/add_patient.html')


def get_patient(request, id):
    patient = Patient.objects.get(pk=id)
    try:
        all_intervention = Detail_patient.objects.filter(patient_id=id)
    except Detail_patient.DoesNotExist:
        all_intervention = None
    try:
        horaire = Horaire.objects.filter(patient_id=id)
    except Horaire.DoesNotExist:
        horaire = None
    lesions = Lesions.objects.all()
    signe_list = Signe_de_vie.objects.all()
    return render(request, 'patient/dossier_patient.html', {'patient': patient, 'interventions': all_intervention,
                                                            'horaires': horaire, 'lesion': lesions, 'signe_vie': signe_list})


def add_intervention(request, id):
    perso = Patient.objects.get(pk=id)
    all_personnels = Personnel.objects.all()
    return render(request, 'patient/add_intervention.html', {'personne': perso, 'personnels': all_personnels})


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
                                                       origine_appel=origine_appel,
                                                       lieu_intervention=lieu_intervention,
                                                       decision=decision,
                                                       trajet=trajet,
                                                       numero_ambulance=numero_ambulance,
                                                       diagnostique_evoque=diagnostique,
                                                       patient_id=perso
                                                       )

        pat = {'patient': perso}
        return render(request, 'patient/dossier_patient.html', pat)


def add_horaire(request, id):
    perso = Patient.objects.get(pk=id)
    return render(request, 'patient/add_horaire.html', {'personne': perso})


def save_horaire(request):
    if request.method == 'POST':
        perso = Patient.objects.get(pk=request.POST['patient_id'])
        Horaire.objects.create(libelle=request.POST['libelle_horaire'],
                               heure=request.POST['heure'],
                               patient_id=perso)
    perso = Patient.objects.get(pk=request.POST['patient_id'])
    return render(request, 'patient/add_horaire.html', {'personne': perso})


def add_lesion(request):
    return render(request, 'patient/add_lesion.html')


def save_lesion(request):
    if request.method == 'POST':
        Lesions.objects.create(libelle_lesion=request.POST['nom_lesion'])
    return render(request, 'patient/add_lesion.html')


def add_organe(request, lesion, patient):
    perso = Patient.objects.get(pk=patient)
    lesion = Lesions.objects.get(pk=lesion)
    try:
        all_diagnostiques = Diagnostique_lesion_organe.objects.filter(patient_id=perso, lesion_id=lesion)
    except Diagnostique_lesion_organe.DoesNotExist:
        all_diagnostiques = None
    return render(request, 'patient/add_organe.html', {'pat': perso, 'les': lesion, 'diagnostiques': all_diagnostiques})

def save_organe_diognostique(request):
    perso = Patient.objects.get(pk=request.POST['patient_id'])
    lesion = Lesions.objects.get(pk=request.POST['lesion_id'])
    if request.method == 'POST':
        Diagnostique_lesion_organe.objects.create(
            nom_organe=request.POST['nom_organe'],
            resultat_diagnostique=request.POST['diagnostique'],
            lesion_id=lesion,
            patient_id=perso
        )
    # return redirect('/save_organe_diognostique')
    try:
        all_diagnostiques = Diagnostique_lesion_organe.objects.filter(patient_id=request.POST['patient_id'])
    except Diagnostique_lesion_organe.DoesNotExist:
        all_diagnostiques = None
    return render(request, 'patient/add_organe.html', {'pat': perso, 'les': lesion, 'diagnostiques': all_diagnostiques})

def add_signe_de_vie(request):
    return render(request, 'patient/signe_de_vie.html')

def save_signe_vie(request):
    if request.method == 'POST':
        Signe_de_vie.objects.create(
            libelle_signe = request.POST['nom_signe_de_vie'],
            description = request.POST['description']
        )
    return render(request, 'patient/signe_de_vie.html')

def ajout_sous_rubrique(request, patient, signe_vie):
    perso = Patient.objects.get(pk=patient)
    signeVie = Signe_de_vie.objects.get(pk=signe_vie)
    return render(request, 'patient/sous_rubrique.html', {'pat': perso, 'signe': signeVie})

def save_score_sous_rubrique(request):
    #perso = Patient.objects.get(pk=request.method['patient_id'])
    signeVie = Signe_de_vie.objects.get(pk=request.method['signe_id'])
    if request.method == 'POST':
        Rubrique_signe_de_vie.objects.create(
            nom_rubrique = request.POST['libelle_sous_rubrique'],
            score = request.POST['score'],
            commentaire_score=request.POST['commentaire_sous_rub'],
            signe_de_vie_id=signeVie
        )

    return render(request, 'patient/sous_rubrique.html', {'signe': signeVie})
