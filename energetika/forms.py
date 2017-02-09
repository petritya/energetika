from django import forms
from django.forms.models import ModelForm
from .models import Megrendeles

class MegrendelesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MegrendelesForm, self).__init__(*args, **kwargs)
        # Making name required
        self.fields['azonosito'].required = True

    class Meta:
        model = Megrendeles
        fields = ['azonosito', 'megrendeloNeve', 'ingatlanIrszam', 'ingatlanVaros', 'ingatlanCim', 'felmeresNapja', 'felmeresIdopontja', 'felmeresDija']