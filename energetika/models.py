from django.db import models

class Megrendeles(models.Model):
    azonosito = models.CharField("Azonosító", max_length=10, unique=True)
    megrendeloNeve = models.CharField("Megrendelő neve", max_length=100)
    ingatlanIrszam = models.IntegerField()
    ingatlanVaros = models.CharField("Ingatlan város", max_length=100)
    ingatlanCim = models.CharField("Ingatlan Cím", max_length=100)
    felmeresNapja = models.DateField(blank=True, null=True)
    felmeresIdopontja = models.TimeField(blank=True, null=True)
    felmeresDija = models.IntegerField()
    
    def __str__(self):
        return self.azonosito
    
class Iranyitoszam(models.Model):
    irSzam = models.IntegerField()
    varos = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.varos