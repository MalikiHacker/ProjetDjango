from django.db import models
from django.contrib.auth.models import User

class Etudiant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    niveau = models.ForeignKey('Niveau', on_delete=models.CASCADE)
    STUDENT = 'ST'
    ROLE = [
        (STUDENT, 'ST')
    ]
    role = models.CharField(
        max_length=2,
        choices=ROLE,
        default=STUDENT,
    )


    def __str__(self):
        return self.user.first_name + '  ' + self.user.last_name + ' ' + self.niveau


class Professeur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact = models.DecimalField(max_digits=9, decimal_places=0)
    TEACHER = 'TE'
    ROLE = [
        (TEACHER, 'TE')
    ]
    role = models.CharField(
        max_length=2,
        choices=ROLE,
        default=TEACHER,
    )

    def __str__(self):
        return self.user.first_name + '  ' + self.user.last_name + ' ' + self.contact

class Salle(models.Model):
    nom_salle = models.CharField(max_length=30)

    def __str__(self):
        return self.nom_salle

class TextBook(models.Model):
    nom_cahier = models.CharField(max_length=25, default="", editable=False)
    nom_niveau = models.ForeignKey('Niveau', on_delete=models.CASCADE)
    gerant = models.ForeignKey(Professeur, on_delete=models.CASCADE)

    def __str__(self):
        return 'Cahier de texte concernant '+self.nom_cahier+' de la classe'+self.nom_niveau+'gere par '+self.gerant

class Niveau(models.Model):
    nom_niveau = models.CharField(max_length=30, primary_key=True)
    responsable_pedagogique = models.ForeignKey(Professeur, on_delete=models.CASCADE)
    cahier = models.ForeignKey(TextBook, on_delete=models.CASCADE)

    def __str__(self):
        return  self.nom_niveau+' gere par '+self.responsable_pedagogique



class Cours(models.Model):
    titre = models.CharField(max_length=30)
    cahier = models.ForeignKey(TextBook, on_delete=models.CASCADE)
    tab_bord = models.DecimalField(max_digits=4, decimal_places=2)
    salle = models.ForeignKey(Salle, on_delete=models.CASCADE)
    professeur = models.ForeignKey(Professeur, on_delete=models.CASCADE)
    duree = models.IntegerField()
    etudiant = models.ManyToManyField(Etudiant, through='Note')

    def __str__(self):
        return self.titre+' de Monsieur '+self.professeur+' avec un duree en heure de '+self.duree

class Note(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE)
    valeur = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return 'Note de l\'etudiant '+self.etudiant+' concernant le cours '+self.cours+' : '+self.valeur


# Create your models here.
