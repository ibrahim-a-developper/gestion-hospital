from django import forms

from personne.models import Docteur, Personne


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

    specialite = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'specialite', 'id': 'validationCustom05'}),
        required=True, max_length=8
    )
    class Meta:
        model = Docteur
        fields = ['num','nom','prenom','tel','adresse','specialite']


    def clean_tel(self):
        num_tel=self.cleaned_data['tel']
        try:
            Personne.objects.get(tel=num_tel)
        except:
            raise forms.ValidationError(f"numero  deja exist")

        if len(num_tel) <8:
            raise forms.ValidationError(f"numpppppppppp")

        return self.cleaned_data['tel']

    # def clean_tel(self):
    #     cd = self.cleaned_data
    #     if(Personne.objects.filter(tel=cd['tel']).exists()):
    #         raise forms.ValidationError(f"Numero Serie existe deja ")
    #     return cd['tel']



