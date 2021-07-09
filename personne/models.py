from django.utils import timezone

from django.db import models
# Create your models here.

class Personne(models.Model):
    num = models.IntegerField()
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    tel = models.IntegerField()
    adresse = models.CharField(max_length=50)

    def __str__(self):
        return '%s' %(self.nom)


class Docteur(Personne):
    specialite = models.ForeignKey('Specialite', on_delete=models.CASCADE, related_name='docteur_specialite')


class Service(models.Model):
    code = models.CharField(max_length=20, verbose_name="Code")
    nom_service = models.CharField(max_length=20)
    batiment = models.CharField(max_length=20)
    directeur = models.ForeignKey(Docteur, on_delete=models.CASCADE, related_name='directeur_service')


    def __str__(self):
        return '%s' % (self.nom_service)


class Infermier(Personne):
    rotation = models.CharField(max_length=50)
    salaire = models.FloatField()
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='infermier_service')

class Maladie(Personne):
    date_entree=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return '{} {}'.format(self.prenom, self.nom)


class Salle(models.Model):
    numero_salle= models.IntegerField()
    nom_service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='salle_service')
    nom_infermier = models.ForeignKey(Infermier, on_delete=models.CASCADE, related_name='salle_infermier')

    def __str__(self):
        return '%s' % (self.numero_salle)

  # date=models.DateTimeField(auto_now=True, blank=True, null=True)
class Hospitaliser(models.Model):
    numero_lit = models.IntegerField()
    diagnostic = models.CharField(max_length=20)
    date=models.DateTimeField(default=timezone.now)
    nom_maladie = models.ForeignKey(Maladie, on_delete=models.CASCADE, related_name='hospitaliser_maladie')
    nom_salle = models.ForeignKey(Salle, on_delete=models.CASCADE, related_name='hospitaliser_salle',verbose_name='Numero salle')

    def __str__(self):
        return '%s' % (self.numero_lit)

class Specialite(models.Model):
    specialite=models.CharField(max_length=20)
    def __str__(self):
        return '%s' % (self.specialite)









