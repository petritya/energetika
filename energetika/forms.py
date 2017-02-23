from django.forms.models import ModelForm
from django import forms
from .models import Megrendeles, Felmeres

class MegrendelesForm(ModelForm):
    
    class Meta:
        model = Megrendeles
        fields = ['azonosito', 'megrendeloNeve', 'megrendeloTelSzam', 'ingatlanIrszam', 'ingatlanVaros', 'ingatlanCim', 'felmeresNapja', 'felmeresIdopontja',
                  'felmeresDija']

class FelmeresForm(ModelForm):

    class Meta:
        model = Felmeres
        fields = ['azonosito', 'telSzamFutar', 'hRSZ', 'szla', 'megrendeloIrszam', 'megrendeloVaros', 'megrendeloCim', 'szallitasiIrszam',
                  'szallitasiVaros', 'szallitasiCim', 'sMSTelSzam', 'bmPince', 'bmFsz', 'bmEmelet', 'teruletPince','teruletFsz',
                  'teruletEmelet', 'padloHoszig', 'padloFutott', 'padloFutetlenPince', 'padloFutetlen', 'padloAnyagFa', 'padloAnyagBeton',
                  'padloAnyagAcel', 'padloAnyagTegla', 'fodemHoszig', 'fodemFutott', 'fodemFutetlenPadlas', 'fodemFutetlen', 'fodemAnyagFa',
                  'fodemAnyagBeton', 'fodemAnyagAcel', 'fodemAnyagTegla', 'futesHelyeKivul', 'futesHelyeBelul', 'futes', 'melegVizHelyeKivul',
                  'melegVizHelyeBelul', 'melegViz', 'epitesEve', 'hoszig', 'fal', 'teruletTulLap', 'szK', 'a', 'v', 'u', 'nyilasZBeepites',
                  'nyilasZUj', 'nyilasZRegi', 'nyilasZ1x', 'nyilasZ2x', 'nyilasZ3x', 'nyilasZ4x', 'nyilasZFa', 'nyilasZPVC', 'nyilasZFem',
                  'ajtoUveg', 'ajtoUj', 'ajtoRegi', 'ajto1x', 'ajto2x', 'ajto3x', 'ajto4x', 'ajtoFa', 'ajtoPVC', 'ajtoFem']

class NyomtatForm(forms.Form):
    FORMAT_CHOICES = (
        ('pdf', 'PDF'),
        ('docx', 'MS Word'),
        ('html', 'HTML'),
    )
    
    felmeres = forms.ModelChoiceField(queryset=Felmeres.objects.all())
    format = forms.ChoiceField(choices=FORMAT_CHOICES)