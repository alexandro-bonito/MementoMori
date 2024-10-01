from django.contrib import admin
from .models import CustomUser, Disciple

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_active', 'is_superuser', 'get_connection_status')

    def get_connection_status(self, obj):
        # Renvoie 'Connecté' ou 'Déconnecté' en fonction de l'état de l'utilisateur
        return 'Connecté' if obj.is_authenticated else 'Déconnecté'
    
    get_connection_status.short_description = 'Statut de connexion'

class DiscipleAdmin(admin.ModelAdmin):
    list_display = ('user', 'numero_whatsapp', 'created_at')

# Enregistrement des modèles avec les classes d'administration personnalisées
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Disciple, DiscipleAdmin)



from django.contrib import admin
from .models import  UserPayment  # Assure-toi d'importer UserPayment

class UserPaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'capture_paiement', 'mot_secret', 'objectif', 'desir_a_realiser', 'date_ajout')
    search_fields = ('user__username', 'objectif', 'desir_a_realiser')  # Permet de rechercher par utilisateur et par objectif
    list_filter = ('date_ajout',)  # Filtrer par date

admin.site.register(UserPayment, UserPaymentAdmin)  # Enregistrement de UserPayment



from django.contrib import admin
from .models import Counter,Decompte

admin.site.register(Counter)
admin.site.register(Decompte)
