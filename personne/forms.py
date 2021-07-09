from django import forms

from personne.models import Docteur, Personne, Hospitaliser, Infermier, Maladie, Salle, Service, Specialite


class DoctorForm(forms.ModelForm):
    tel=forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'tel', 'id':'validationCustom01'} ),
        required=True, max_length=8
    )

    adresse = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'adresse', 'id': 'validationCustom02'}),
        required=True, max_length=8
    )

    nom = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'nom', 'id': 'validationCustom03'}),
        required=True, max_length=8
    )

    prenom = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'prenom', 'id': 'validationCustom04'}),
        required=True, max_length=8
    )


    class Meta:
        model = Docteur
        fields = ['num','nom','prenom','tel','adresse','specialite']


    # def clean_tel(self):
    #     num_tel=self.cleaned_data['tel']
    #     try:
    #         Personne.objects.get(tel=num_tel)
    #     except:
    #         raise forms.ValidationError(f"numero  deja exist")
    #
    #     if len(num_tel) <8:
    #         raise forms.ValidationError(f"le numero telephone ne dois pas etre inferier a 8 chiffres")
    #
    #     return self.cleaned_data['tel']

    # def clean_tel(self):
    #     cd = self.cleaned_data
    #     if(Personne.objects.filter(tel=cd['tel']).exists()):
    #         raise forms.ValidationError(f"Numero Serie existe deja ")
    #     return cd['tel']


#hospitialiser
class HospitialiserForm(forms.ModelForm):
    class Meta:
        model = Hospitaliser
        fields = ['nom_maladie','nom_salle','diagnostic','numero_lit']

    # def clean_numero_lit(self):
    #     numero_lit = self.cleaned_data.get('numero_lit')
    #     nom_salle = self.cleaned_data.get('nom_salle')
    #     if (numero_lit) and (nom_salle):
    #         raise forms.ValidationError("cette place est deja reservee")
    #     return numero_lit
    def clean_numero_lit(self):
        cd = self.cleaned_data
        if ((Hospitaliser.objects.filter(numero_lit=cd['numero_lit']).exists()) and (
        Hospitaliser.objects.filter(nom_salle=cd['nom_salle']).exists())):
            raise forms.ValidationError(f" cette place est deja reservee")
        return cd['numero_lit']


# hospitialiser2
class HospitialiserFormm(forms.ModelForm):
    class Meta:
        model = Hospitaliser
        fields = ['nom_salle', 'diagnostic', 'numero_lit']
    #
    # def clean_numero_lit(self):
    #     numero_lit = self.cleaned_data.get('numero_lit')
    #     nom_salle = self.cleaned_data.get('nom_salle')
    #     if (numero_lit) and (nom_salle):
    #         raise forms.ValidationError("cette place est deja reservee")
    #     return numero_lit
    def clean_numero_lit(self):
        cd = self.cleaned_data
        if ((Hospitaliser.objects.filter(numero_lit=cd['numero_lit']).exists()) and (
        Hospitaliser.objects.filter(nom_salle=cd['nom_salle']).exists())):
            raise forms.ValidationError(f" cette place est deja reservee")
        return cd['numero_lit']


#infermiere
class InfermierForm(forms.ModelForm):
    class Meta:
        model = Infermier
        fields = ['rotation','salaire','service']

#maladie
class MaladieForm(forms.ModelForm):
    class Meta:
        model = Maladie
        fields = fields = ['num','nom','prenom','tel','adresse']

#salle
class SalleForm(forms.ModelForm):
    class Meta:
        model = Salle
        fields = fields = ['numero_salle','nom_service','nom_infermier']

#service
class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = fields = ['code','nom_service','batiment','directeur']

#specialite
class SpecialiteForm(forms.ModelForm):
    class Meta:
        model = Specialite
        fields = fields = ['specialite',]

    def clean_specialite(self):
        cd = self.cleaned_data
        # mot=Specialite.objects.filter(specialite=cd['specialite']).exists()
        # m=mot.Upper()
        if (Specialite.objects.filter(specialite=cd['specialite']).exists()):
            raise forms.ValidationError(f" deja existe")
        return cd['specialite']
