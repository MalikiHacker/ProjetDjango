from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ValidationError
from PlanninGO.models import Etudiant, Professeur, TextBook, Salle, Niveau, Cours
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def Accueil(request):
    return render(request, 'index.html')


def save(request):
    if request.GET['role'] == '1':
        newEtudiant = Etudiant()
        newUser = User()
        newNiveau = Niveau.objects.get(nom_niveau=request.GET['niveau'])
        newUser.first_name = request.GET['prenom']
        newUser.last_name = request.GET['nom']
        newUser.username = request.GET['username']
        newUser.email = request.GET['email']
        newUser.set_password(request.GET['password'])

        newEtudiant.user = newUser
        newUser.save()

        newBook = TextBook()
        newNiveau.cahier = newBook
        newEtudiant.niveau = newNiveau

        newEtudiant.save()
        if newUser.email.endswith('@ept.sn') and newUser.password:
            return render(request, 'connexion.html')
        else:
            raise ValidationError('Format d\'email ou mot de passe invalide !! Veuillez respecter le format recommende')
            newUser.delete()
            newBook.delete()
            newEtudiant.delete()
    elif request.GET['role'] == '2':
        newProfesseur = Professeur()
        newUser = User()
        newUser.first_name = request.GET['prenom']
        newUser.last_name = request.GET['nom']
        newUser.username = request.GET['username']
        newUser.email = request.GET['email']
        newUser.set_password(request.GET['password'])

        newProfesseur.user = newUser
        newUser.save()
        newProfesseur.save()
        if newUser.email.endswith('@ept.sn') and newUser.password:
            return render(request, 'connexion.html')
        else:
            raise ValidationError('Format d\'email ou mot de passe invalide !! Veuillez respecter le format recommende')
            newUser.delete()
            newBook.delete()
            newProfesseur.delete()
            return render(request, 'inscription.html')
# Create your views here.
def Inscription(request):
    return render(request, 'inscription.html')


def Connexion(request):
    return render(request, 'connexion.html')


def loginpage(request):
    username = request.POST['username']
    password = request.POST['password']
    role = request.POST['role']
    user = authenticate(username=username, password=password)
    if user is not None and user.is_active:
        login(request, user)
        query = get_object_or_404(User, username=username)
        etudiants = Etudiant.objects.all()
        if role == '1':
            return render(request, 'index_eleve.html', {'query': query, 'etudiants': etudiants})
        else:
            return render(request, 'index_prof.html', {'query': query, 'etudiants': etudiants})
    else:
        return render(request, 'connexion.html')


def logoutpage(request):
    try:
        logout(request)
    except:
        pass
    return render(request, 'index.html')

def show_cours(request):
    courses = Cours.objects.all()

    return render(request, 'emploi_temps.html', {'courses': courses})


def update(request, id):
    course = get_object_or_404(Cours, pk=id)
    return render(request, 'edit.html', {'course': course})

