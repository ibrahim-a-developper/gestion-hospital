from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from personne.forms import DoctorForm
from personne.models import Docteur, Infermier, Service, Salle, Personne


#view home
def home(request):
    #selectionner
    docteur= Docteur.objects.all()
    infermier= Infermier.objects.all()
    service= Service.objects.all()
    salle= Salle.objects.all()

    #counter
    nbr_docteur= docteur.count()
    nbr_infermier=infermier.count()
    nbr_service = service.count()
    nbr_salle = salle.count()

    context = {
        'nbr_docteur': nbr_docteur,
        'nbr_infermier': nbr_infermier,
        'nbr_service': nbr_service,
        'nbr_salle': nbr_salle,
    }
    return render(request, 'index.html',context)


#add doctor
'''
def add_docteur(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, f"L'equipemet du numero  est bien ajoute")
            return redirect(reverse('personne:add_docteur'))
        else:
            messages.error(request, "Un erreur se produire")
    else:
        form = DoctorForm()

    return render(request, 'add_docteur.html', {'form': form})

'''

def add_docteur(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f"L'equipemet du numero est bien ajoute")
            return redirect('personne:add_docteur')
        else:
            messages.error(request, f"Un erreur se produire")
    else:
        form = DoctorForm()

    return render(request, 'add_docteur1.html', {'form': form})

#list docteur
def list_docteur(request):
    docteurs= Docteur.objects.all()
    context={
        'docteurs':docteurs,
    }
    return render(request, 'list_docteur1.html', context)


def list_personne(request):
    personnes= Personne.objects.all()
    context={
        'personnes':personnes,
    }
    return render(request, 'list_personne.html', context)