
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse

from personne.forms import DoctorForm, HospitialiserForm, InfermierForm, MaladieForm, SalleForm, ServiceForm, \
    SpecialiteForm, HospitialiserFormm
from personne.models import Docteur, Infermier, Service, Salle, Personne, Specialite, Maladie, Hospitaliser


#view home
@login_required(login_url='accounts/login')
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

    #pagination
    paginator = Paginator(service, 3)
    page_numbre = request.GET.get('page')
    page_obj = paginator.get_page(page_numbre)

    context = {
        'nbr_docteur': nbr_docteur,
        'nbr_infermier': nbr_infermier,
        'nbr_service': nbr_service,
        'nbr_salle': nbr_salle,
        'service':service,
        'list_direction': page_obj,
    }
    return render(request, 'index.html',context)


###################################
#Add                              #
###################################

#Docteur
def add_docteur(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Docteur est bien ajouter")
            return redirect('personne:add_docteur')
        else:
            messages.error(request, f"L'insertion n'est pas bin marche")
    else:
        form = DoctorForm()
    return render(request, 'add_docteur1.html', {'form': form})

#hospitialiser
def add_hospitialiser(request):
    h=Hospitaliser.objects.all()
    if request.method == 'POST':
        form = HospitialiserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Hospitialiser est bien ajouter")
            return redirect('personne:add_hospitialiser')
        else:
            messages.error(request, f"L'insertion n'est pas bin marche")
    else:
        form = HospitialiserForm()

    return render(request, 'add_hospitaliser.html',  {'form': form})

#infermiere
def add_infermiere(request):
    if request.method == 'POST':
        form = InfermierForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Infermiere est bien ajouter")
            return redirect('personne:add_infermiere')
        else:
            messages.error(request, f"L'insertion n'est pas bin marche")
    else:
        form = InfermierForm()
    return render(request, 'add_infermier.html', {'form': form})

#maladie
def add_maladie(request):
    if request.method == 'POST':
        form = MaladieForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Infermiere est bien ajouter")
            return redirect('personne:add_maladie')
        else:
            messages.error(request, f"L'insertion n'est pas bin marche")
    else:
        form = MaladieForm()
    return render(request, 'add_maladie.html', {'form': form})

#salle
def add_salle(request):
    if request.method == 'POST':
        form = SalleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Service est bien ajouter")
            return redirect('personne:add_salle')
        else:
            messages.error(request, f"L'insertion n'est pas bin marche")
    else:
        form = SalleForm()
    return render(request, 'add_salle.html', {'form': form})

#service
def add_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Salle est bien ajouter")
            return redirect('personne:add_service')
        else:
            messages.error(request, f"L'insertion n'est pas bin marche")
    else:
        form = ServiceForm()
    return render(request, 'add_service.html', {'form': form})

#specialite
def add_specialite(request):
    if request.method == 'POST':
        form = SpecialiteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Specialite est bien ajouter")
            return redirect('personne:add_specialite')
        else:
            messages.error(request, f"L'insertion n'est pas bin marche")
    else:
        form = SpecialiteForm()
    return render(request, 'add_specialite.html', {'form': form})



###################################
#tables                           #
###################################
#docteur
def list_docteur(request):
    docteurs= Docteur.objects.all()
    context={
        'docteurs':docteurs,
    }
    return render(request, 'list_docteur1.html', context)

#hospitialiser
def list_hospitialiser(request):
    hospitialisers= Hospitaliser.objects.all()
    context={
        'hospitialisers':hospitialisers,
    }
    return render(request, 'list_hospitialiser.html', context)

#Infermier
def list_infermier(request):
    infermiers= Infermier.objects.all()
    context={
        'infermiers':infermiers,
    }
    return render(request, 'list_infermier.html', context)

#Maladie
def list_maladie(request):
    maladies= Maladie.objects.all()
    context={
        'maladies':maladies,
    }
    return render(request, 'list_maladie.html', context)

#Service
def list_service(request):
    services= Service.objects.all()
    salles=Salle.objects.all()
    context={
        'services':services,
        'salles':salles,
    }
    return render(request, 'list_service.html', context)

#salle_specialite
def list_salle_specialite(request):
    salles= Salle.objects.all()
    specialites = Specialite.objects.all()
    context={
        'salles':salles,
        'specialites': specialites,
    }
    return render(request, 'list_salle_specialite.html', context)


def list_personne(request):
    personnes= Personne.objects.all()
    context={
        'personnes':personnes,
    }
    return render(request, 'list_personne.html', context)

###################################
#Delete                          #
###################################
#docteur
def DocteurDeleteView(request, docteur_id):
    docteur=Docteur.objects.get(id=docteur_id)
    if request.method == 'POST':
        docteur.delete()
        messages.success(
            request, f"Felicitation l'equipemet avec numero  {docteur.nom} est bien supprimer")
        return redirect('personne:list_docteur')
    context = {
        'title': 'Supprimer docteur',
        'docteur': docteur
        }
    return render(request,'docteur_confirm_delete.html', context)

#hospitialiser
def HospitialiserDeleteView(request, docteur_id):
    docteur=Hospitaliser.objects.get(id=docteur_id)
    if request.method == 'POST':
        docteur.delete()
        messages.success(
            request, f"Felicitation la suppression est bien marche")
        return redirect('personne:list_hospitialiser')
    context = {
        'title': 'Supprimer hospitialiser',
        'docteur': docteur
        }
    return render(request,'hospitialiser_confirm_delete.html', context)

#infermier
def InfermierDeleteView(request, docteur_id):
    docteur=Infermier.objects.get(id=docteur_id)
    if request.method == 'POST':
        docteur.delete()
        messages.success(
            request, f"Felicitation la suppression est bien marche")
        return redirect('personne:list_infermier')
    context = {
        'title': 'Supprimer infermier',
        'docteur': docteur
        }
    return render(request,'infermier_confirm_delete.html', context)

#maladie
def MaladieDeleteView(request, docteur_id):
    docteur=Maladie.objects.get(id=docteur_id)
    if request.method == 'POST':
        docteur.delete()
        messages.success(
            request, f"Felicitation la suppression est bien marche")
        return redirect('personne:list_maladie')
    context = {
        'title': 'Supprimer maladie',
        'docteur': docteur
        }
    return render(request,'maladie_confirm_delete.html', context)

#salle
def SalleDeleteView(request, docteur_id):
    docteur=Salle.objects.get(id=docteur_id)
    if request.method == 'POST':
        docteur.delete()
        messages.success(
            request, f"Felicitation la suppression est bien marche")
        return redirect('personne:list_salle_specialite')
    context = {
        'title': 'Supprimer salle',
        'docteur': docteur
        }
    return render(request,'salle_confirm_delete.html', context)

#specialite
def SpecialiteDeleteView(request, docteur_id):
    docteur=Specialite.objects.get(id=docteur_id)
    if request.method == 'POST':
        docteur.delete()
        messages.success(
            request, f"Felicitation la suppression est bien marche")
        return redirect('personne:list_salle_specialite')
    context = {
        'title': 'Supprimer specialite',
        'docteur': docteur
        }
    return render(request,'specialite_confirm_delete.html', context)

#service
def ServiceDeleteView(request, docteur_id):
    docteur=Service.objects.get(id=docteur_id)
    if request.method == 'POST':
        docteur.delete()
        messages.success(
            request, f"Felicitation la suppression est bien marche")
        return redirect('personne:list_service')
    context = {
        'title': 'Supprimer service',
        'docteur': docteur
        }
    return render(request,'service_confirm_delete.html', context)







###################################
#Update                           #
###################################
#docteur
def DocteurUpdate(request, docteur_id):
    docteur=Docteur.objects.get(id=docteur_id)
    form=DoctorForm(instance=docteur)

    if request.method == 'POST':
        form=DoctorForm(request.POST, instance=docteur)
        if form.is_valid():
            form.save()
            messages.success(
                request, f"Felicitation categorie {docteur.nom} est bien modifier")
            return redirect('personne:list_docteur')
        else:
            messages.error(request, f"une erreur c'est prouit dun la serveur  reactialiser la page")
    context = {
        'title': 'Modifier docteur',
        'form': form
        }
    return render(request,'update_docteur.html', context)

#hospitialiser
def HospitaliserUpdate(request, docteur_id):
    docteur=Hospitaliser.objects.get(id=docteur_id)
    form=HospitialiserForm(instance=docteur)
    if request.method == 'POST':
        form=HospitialiserForm(request.POST, instance=docteur)
        if form.is_valid():
            form.save()
            messages.success(
                request, f"Felicitation la modification est bien marche")
            return redirect('personne:list_hospitialiser')
        else:
            messages.error(request, f"une erreur c'est prouit dun la serveur  reactialiser la page")
    context = {
        'title': 'Modifier ',
        'form': form
        }
    return render(request,'update_hospitialiser.html', context)

#infermier
def InfermierUpdate(request, docteur_id):
    docteur=Infermier.objects.get(id=docteur_id)
    form=InfermierForm(instance=docteur)
    if request.method == 'POST':
        form=InfermierForm(request.POST, instance=docteur)
        if form.is_valid():
            form.save()
            messages.success(
                request, f"Felicitation la modification est bien marche")
            return redirect('personne:list_infermier')
        else:
            messages.error(request, f"une erreur c'est prouit dun la serveur  reactialiser la page")
    context = {
        'title': 'Modifier infermier',
        'form': form
        }
    return render(request,'update_infermier.html', context)

#maladie
def MaladieUpdate(request, docteur_id):
    docteur=Maladie.objects.get(id=docteur_id)
    form=MaladieForm(instance=docteur)
    if request.method == 'POST':
        form=MaladieForm(request.POST, instance=docteur)
        if form.is_valid():
            form.save()
            messages.success(
                request, f"Felicitation la modification est bien marche")
            return redirect('personne:list_maladie')
        else:
            messages.error(request, f"une erreur c'est prouit dun la serveur  reactialiser la page")
    context = {
        'title': 'Modifier maladie',
        'form': form
        }
    return render(request,'update_maladie.html', context)


#salle
def SalleUpdate(request, docteur_id):
    docteur=Salle.objects.get(id=docteur_id)
    form=SalleForm(instance=docteur)
    if request.method == 'POST':
        form=SalleForm(request.POST, instance=docteur)
        if form.is_valid():
            form.save()
            messages.success(
                request, f"Felicitation la modification est bien marche")
            return redirect('personne:list_salle_specialite')
        else:
            messages.error(request, f"une erreur c'est prouit dun la serveur  reactialiser la page")
    context = {
        'title': 'Modifier salle',
        'form': form
        }
    return render(request,'update_salle.html', context)

#specialite
def SpecialiteUpdate(request, docteur_id):
    docteur=Specialite.objects.get(id=docteur_id)
    form=SpecialiteForm(instance=docteur)
    if request.method == 'POST':
        form=SpecialiteForm(request.POST, instance=docteur)
        if form.is_valid():
            form.save()
            messages.success(
                request, f"Felicitation la modification est bien marche")
            return redirect('personne:list_salle_specialite')
        else:
            messages.error(request, f"une erreur c'est prouit dun la serveur  reactialiser la page")
    context = {
        'title': 'Modifier specialite',
        'form': form
        }
    return render(request,'update_specialite.html', context)

#service
def ServiceUpdate(request, docteur_id):
    docteur=Service.objects.get(id=docteur_id)
    form=ServiceForm(instance=docteur)
    if request.method == 'POST':
        form=ServiceForm(request.POST, instance=docteur)
        if form.is_valid():
            form.save()
            messages.success(
                request, f"Felicitation la modification est bien marche")
            return redirect('personne:list_service')
        else:
            messages.error(request, f"une erreur c'est prouit dun la serveur  reactialiser la page")
    context = {
        'title': 'Modifier service',
        'form': form
        }
    return render(request,'update_service.html', context)



###################################
#View                            #
###################################
#docteur
def DocteurDetail(request, docteur_id):
    detail_docteur= get_object_or_404(Docteur, pk=docteur_id)
    context = {
        'title': 'detail docteur',
        'detail_docteur': detail_docteur,
    }

    return render(request, 'detail_docteur.html', context)

#service
def ServiceDetail(request, service_id):
    detail_service= get_object_or_404(Service, pk=service_id)
    salles=Salle.objects.filter(nom_service=service_id)

    context = {
        'title': 'detail service',
        'detail_service': detail_service,
        'salles':salles,
    }
    return render(request, 'detail_service.html', context)

#maladie
def MaladieDetail(request, maladie_id):
    detail_maladie= get_object_or_404(Maladie, pk=maladie_id)
    maladie_hospitialiser =Hospitaliser.objects.filter(nom_maladie=maladie_id)

    try:
        h = Hospitaliser.objects.get(nom_maladie=maladie_id)
    except Hospitaliser.DoesNotExist:
        h = None

    # salles=Salle.objects.filter(nom_service=service_id)
    # eeeeeeeeeeeeeeeeeeee
    if request.method == 'POST':
        form = HospitialiserFormm(data=request.POST)
        if form.is_valid():
            # hospitaliser_maladie
            e=form.save(commit=False)
            e.nom_maladie=detail_maladie
            e.save()
            messages.success(request, f"Hospitialiser est bien ajouter")
            return redirect('personne:detail_maladie',maladie_id)
        else:
            messages.error(request, f"L'insertion n'est pas bin marche")
    else:
        form = HospitialiserFormm()
   #eeeeeeeeeeeeeeeeeee
    context = {
        'title': 'detail maladie',
        'detail_maladie': detail_maladie,
        'maladie_hospitialiser':maladie_hospitialiser,
        'form':form,
        'h':h,
    }
    return render(request, 'detail_maladie.html', context)