import uuid
from django.db import models

class Journal(models.Model):
    class TypeJournal(models.TextChoices):
        ACHATS = 'achats', 'Achats'
        VENTES = 'ventes', 'Ventes'
        CAISSE = 'caisse', 'Caisse'
        BANQUE = 'banque', 'Banque'
        OD = 'od', 'Opérations Diverses'

    code = models.CharField(max_length=10, primary_key=True) # ACH, VTE, CAI, BQ, OD, FISC
    libelle = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=TypeJournal.choices)
    succursale = models.ForeignKey('parametres.Succursale', on_delete=models.CASCADE, related_name='journaux')
    dernierNumero = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.code} - {self.libelle}"

class Tiers(models.Model):
    class TypeTiers(models.TextChoices):
        FOURNISSEUR = 'fournisseur', 'Fournisseur'
        CLIENT = 'client', 'Client'
        PERSONNEL = 'personnel', 'Personnel'
        ETAT = 'etat', 'Etat'
        ASSOCIE = 'associe', 'Associé'

    code = models.CharField(max_length=50, primary_key=True)
    nom = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=TypeTiers.choices)
    compte = models.CharField(max_length=50, blank=True, null=True) # Reference to CompteComptable, but can be CharField to avoid circular/hard dependency or FK
    soldeDebit = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    soldeCredit = models.DecimalField(max_digits=15, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.code} - {self.nom}"

class CompteComptable(models.Model):
    class TypeCompte(models.TextChoices):
        GENERAL = 'general', 'Général'
        AUXILIAIRE = 'auxiliaire', 'Auxiliaire'

    numero = models.CharField(max_length=50, primary_key=True)
    libelle = models.CharField(max_length=255)
    classe = models.CharField(max_length=1)
    type = models.CharField(max_length=20, choices=TypeCompte.choices, default=TypeCompte.GENERAL)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name='sous_comptes')
    lettable = models.BooleanField(default=False)
    tiers = models.ForeignKey(Tiers, on_delete=models.SET_NULL, blank=True, null=True, related_name='comptes')
    soldeDebit = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    soldeCredit = models.DecimalField(max_digits=15, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.numero} - {self.libelle}"
