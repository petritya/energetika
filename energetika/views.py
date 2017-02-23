from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from _datetime import datetime

from templated_docs import fill_template
from templated_docs.http import FileResponse

from .forms import MegrendelesForm, FelmeresForm, NyomtatForm
from .models import Megrendeles, Felmeres, Iranyitoszam

@login_required(login_url="login/")
def home(request):
    return render(request, "home.html", {})

def megrendelesek(request):
    template = "megrendelesek.html"
    instance = None
    hiba = False
    osszesdij = 0
    irSzamok = Iranyitoszam.objects.all().order_by('varos')

    if 'megrendelesid' in request.POST:
        pk = request.POST['megrendelesid']
        instance = get_object_or_404(Megrendeles, pk=pk)

    if 'felmereshonapja' in request.POST:
        s = request.POST.get('felmereshonapja', '')
        curr_date = datetime.strptime(s, "%Y-%m").date()
    else:
        curr_date = datetime.now()
        
    if 'reset' in request.POST:
        instance = None
        
    if 'uj_megrendeles' in request.POST:
        form = MegrendelesForm(request.POST)
        irsz = request.POST['ingatlanVaros']
        varos = get_object_or_404(Iranyitoszam, irSzam=irsz)
        if form.is_valid():
            megrendeles = form.save(commit=False)
            megrendeles.ingatlanVaros = varos.varos
            megrendeles.azonosito = megrendeles.azonosito.upper()
            megrendeles.save()
            f = Felmeres.objects.create(megrendeles=megrendeles)
            f.azonosito = megrendeles.azonosito
            f.save()
            template = "megrendelesek.html"
        else:
            hiba = True
    
    if 'megrendeles_modositas' in request.POST:
        pk = request.POST['instanceid']
        megrendeles = get_object_or_404(Megrendeles, pk=pk)
        form = MegrendelesForm(request.POST, instance=megrendeles)
        irsz = request.POST['ingatlanVaros']
        varos = get_object_or_404(Iranyitoszam, irSzam=irsz)
        if form.is_valid():
            megrendeles2 = form.save(commit=False)
            megrendeles2.ingatlanVaros = varos.varos
            megrendeles2.azonosito = megrendeles2.azonosito.upper()
            megrendeles2.save()
            instance = get_object_or_404(Megrendeles, pk=pk)
            template = "megrendelesek.html"

    if 'megrendeles_torles' in request.POST:
        pk = request.POST['instanceid']
        megrendeles = get_object_or_404(Megrendeles, pk=pk)
        megrendeles.delete()
        return redirect('megrendelesek')
          
    results = Megrendeles.objects.filter(felmeresNapja__year=curr_date.year, felmeresNapja__month=curr_date.month).order_by('-felmeresNapja', '-felmeresIdopontja')
    
    for result in results:
        osszesdij += int(result.felmeresDija)
  
    context = {'ido': curr_date, 'megrendelesek': results, 'instance': instance, 'hibauzenet': hiba, 'osszesdij': osszesdij, 'irSzamok': irSzamok}
   
    return render(request, template, context)

def felmeres(request):
    template = "felmeres.html"
    instance = None
    megrendeles = None
    irSzamok = Iranyitoszam.objects.all().order_by('varos')
    
    if 'azonosito' in request.POST:
        azonosito = request.POST['azonosito'].upper()
        instance = get_object_or_404(Felmeres, azonosito=azonosito)
        megrendeles = get_object_or_404(Megrendeles, azonosito=azonosito)
    
    if 'mentes' in request.POST:
        pk = request.POST['instanceid']
        felmeres = get_object_or_404(Felmeres, pk=pk)

        form = FelmeresForm(request.POST, instance=felmeres)

        if request.POST['megrendeloVaros']:
            mirsz = request.POST['megrendeloVaros']
            mv = get_object_or_404(Iranyitoszam, irSzam=mirsz)
            mvaros = mv.varos
        else:
            mvaros = ""
        
        if request.POST['szallitasiVaros']:
            szirsz = request.POST['szallitasiVaros']
            szv = get_object_or_404(Iranyitoszam, irSzam=szirsz)
            szvaros = szv.varos
        else:
            szvaros = ""
            
        if form.is_valid():
            felm = form.save(commit=False)
            felm.megrendeloVaros = mvaros
            felm.szallitasiVaros = szvaros
            felm.save()
            instance = get_object_or_404(Felmeres, pk=pk)
            
    if 'nyomtat' in request.POST:
        form = NyomtatForm(request.POST or None)
        print(form)
        if form.is_valid():
            doctype = form.cleaned_data['format']
            filename = fill_template(
                'nyomtat/felmeresilap.odt', form.cleaned_data,
                output_format=doctype)
            visible_filename = 'felmeresilap.{}'.format(doctype)
    
            return FileResponse(filename, visible_filename)
    
        
    context = {'instance': instance, 'megrendeles': megrendeles, 'irSzamok': irSzamok}
    
    return render(request, template, context)
    
def terulet_sima(request):
    template = "szamolas/terulet_sima.html"
    context = {}
    if 'szamol' in request.POST:
        aoldal = request.POST['aoldal']
        boldal = request.POST['boldal']
        aoldal = float(aoldal.replace(",", "."))
        boldal = float(boldal.replace(",", "."))
        eredmeny = aoldal * boldal
        context = {'eredmeny': eredmeny}
    
    return render(request, template, context)

def terulet_vagott(request):
    template = "szamolas/terulet_vagott.html"
    context = {}
    if 'szamol' in request.POST:
        aoldal = request.POST['aoldal']
        coldal = request.POST['coldal']
        doldal = request.POST['doldal']
        foldal = request.POST['foldal']
        aoldal = float(aoldal.replace(",", "."))
        coldal = float(coldal.replace(",", "."))
        doldal = float(doldal.replace(",", "."))
        foldal = float(foldal.replace(",", "."))
        eredmeny = aoldal * doldal + coldal * foldal
        context = {'eredmeny': eredmeny}
    
    return render(request, template, context)

def tomb(request):
    template = "szamolas/tomb.html"
    context = {}
    if 'szamol' in request.POST:
        aoldal = request.POST['aoldal']
        boldal = request.POST['boldal']
        coldal = request.POST['coldal']
        aoldal = float(aoldal.replace(",", "."))
        boldal = float(boldal.replace(",", "."))
        coldal = float(coldal.replace(",", "."))
        a = 2 * (aoldal * boldal + aoldal * coldal + boldal * coldal)
        v = aoldal * boldal * coldal
        context = {'a': a,'v': v}
    
    return render(request, template, context)

def nyomtat(request):
    form = NyomtatForm(request.POST or None)

    if form.is_valid():
        doctype = form.cleaned_data['format']
        filename = fill_template(
            'nyomtat/felmeresilap.odt', form.cleaned_data,
            output_format=doctype)
        visible_filename = 'felmeresilap.{}'.format(doctype)

        return FileResponse(filename, visible_filename)
    else:
        return render(request, 'nyomtat/form.html', {'form': form})