from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from _datetime import datetime

from .forms import MegrendelesForm
from .models import Megrendeles

@login_required(login_url="login/")
def home(request):
    return render(request, "home.html", {})

def megrendelesek(request):
    template = "megrendelesek.html"
    instance = None
    hiba = False
    osszesdij = 0

    if 'megrendelesid' in request.POST:
        pk = request.POST['megrendelesid']
        instance = get_object_or_404(Megrendeles, azonosito=pk)

    if 'felmereshonapja' in request.POST:
        s = request.POST.get('felmereshonapja', '')
        curr_date = datetime.strptime(s, "%Y-%m").date()
    else:
        curr_date = datetime.now()
        
    if 'reset' in request.POST:
        instance = None
        
    if 'uj_megrendeles' in request.POST:
        form = MegrendelesForm(request.POST)
        if form.is_valid():
            megrendeles = form.save(commit=False)
            megrendeles.save()
            template = "megrendelesek.html"
        else:
            hiba = True

    if 'megrendeles_modositas' in request.POST:
        azonosito = request.POST['azonosito']
        megrendeles = get_object_or_404(Megrendeles, azonosito=azonosito)
        form = MegrendelesForm(request.POST, instance=megrendeles)
        if form.is_valid():
            form.save()
            instance = get_object_or_404(Megrendeles, azonosito=azonosito)
            template = "megrendelesek.html"

    if 'megrendeles_torles' in request.POST:
        megrendeles = get_object_or_404(Megrendeles, pk=pk)
        megrendeles.delete()
        return redirect('megrendelesek')
          
    results = Megrendeles.objects.filter(felmeresNapja__year=curr_date.year, felmeresNapja__month=curr_date.month).order_by('-felmeresNapja', '-felmeresIdopontja')
    
    for result in results:
        osszesdij += int(result.felmeresDija)
  
    context = {'ido': curr_date, 'megrendelesek': results, 'instance': instance, 'hibauzenet': hiba, 'osszesdij': osszesdij}
   
    return render(request, template, context)
