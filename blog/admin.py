from django.contrib import admin
from .models import Peintre, Tableau, Commentaire, Type

# Register your models here.


admin.site.register(Peintre)
admin.site.register(Tableau)
admin.site.register(Commentaire)
admin.site.register(Type)