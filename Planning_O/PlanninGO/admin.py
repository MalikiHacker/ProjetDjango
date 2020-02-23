from django.contrib import admin
from django.apps import apps
from .models import Etudiant, Professeur, Niveau, TextBook, Note

mode = apps.get_models()
for model in mode:
    if mode not in [Niveau, Note, Etudiant]:
        try:
            admin.site.register(model)
        except:
            pass
    else:
        pass

# Register your models here.
