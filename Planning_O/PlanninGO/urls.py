from django.urls import path
from . import views

urlpatterns = [
    path('', views.Accueil, name='accueil'),
    path('login', views.Connexion, name='login'),
    path('login/authentifier', views.loginpage, name='authentifier'),
    path('logout', views.logoutpage, name='logout'),
    path('signin', views.Inscription, name='signin'),
    path('signin/validate', views.save, name='validate'),

]