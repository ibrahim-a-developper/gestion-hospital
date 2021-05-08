from django.contrib import admin

# Register your models here.
from personne.models import Personne, Docteur, Infermier, Service, Maladie, Salle, Hospitaliser

admin.site.register(Personne)
admin.site.register(Docteur)
admin.site.register(Infermier)

admin.site.register(Service)
admin.site.register(Maladie)

admin.site.register(Salle)
admin.site.register(Hospitaliser)