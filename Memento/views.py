from django.shortcuts import render

# Create your views here.
def Mori(request):
    return render(request, 'Mori.html')

def Moria(request):
    return render(request, 'moria.html')
    
from django.shortcuts import render
from .models import Counter, Decompte
from django.shortcuts import render
from .models import Counter, Decompte

def Memenfos(request):
    # Récupérer l'instance du décompte
    decompte = Decompte.objects.first()
    count = Counter.objects.first()

    if decompte:
        decompte.decrement()  # Décrémenter le décompte

    context = {
        'decompte_count': decompte.count if decompte else 46800,
        'count': count,
    }
    return render(request, 'infos.html', context)



from django.contrib.auth import login
from django.contrib.auth import get_backends
from django.http import HttpResponse





from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.http import HttpResponse
from .models import CustomUser, Disciple
from django.db import transaction

def signup_view(request):
    if request.method == 'POST':
        vrai_nom = request.POST.get('vrai_nom')
        vrai_prenom = request.POST.get('vrai_prenom')
        numero_whatsapp = request.POST.get('numero_whatsapp')
        sexe = request.POST.get('sexe')
        date_naissance = request.POST.get('date_naissance')

        if not (vrai_nom and vrai_prenom and numero_whatsapp and sexe and date_naissance):
            return HttpResponse("Tous les champs sont requis.")

        try:
            with transaction.atomic():  # Utilisation d'une transaction
                custom_user = CustomUser.objects.create_user(
                    username=numero_whatsapp,
                    password=numero_whatsapp,
                    first_name=vrai_prenom,
                    last_name=vrai_nom,
                    date_naissance=date_naissance,
                    sexe=sexe,
                )

                Disciple.objects.create(
                    user=custom_user,
                    numero_whatsapp=numero_whatsapp,
                )

                # Connexion automatique de l'utilisateur
                backend = 'Memento.backends.WhatsAppAuthBackend'
                login(request, custom_user, backend=backend)

            return redirect('Moria')  # Redirection après succès

        except Exception as e:
            return HttpResponse(f"Erreur : {e}")

    return render(request, 'signup.html')





from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserPayment
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from .models import UserPayment






from django.shortcuts import render
from .models import Counter
from django.shortcuts import render
from .models import Counter

def show_counter(request):
    counter, created = Counter.objects.get_or_create(id=1)

    context = {
        'count': counter.count,  # Assure-toi que c'est bien ici
    }
    return render(request, 'counter.html', context)
def decrement(self):
    if self.count > 0:
        print(f'Décrémentation : {self.count} -> {self.count - 1}')  # Ajoute un print
        self.count -= 1
        self.save()
