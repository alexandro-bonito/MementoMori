from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    sexe = models.CharField(max_length=10)  # 'M' ou 'F'
    date_naissance = models.DateField(null=True, blank=True)

    # Évitez de redéfinir les champs groups et user_permissions
    # en utilisant un related_name unique si nécessaire
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True,
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        blank=True,
    )
class Disciple(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    numero_whatsapp = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)




from django.db import models
from django.conf import settings

class UserPayment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    capture_paiement = models.ImageField(upload_to='paiements/')
    mot_secret = models.CharField(max_length=255)
    objectif = models.CharField(max_length=255)
    desir_a_realiser = models.TextField()
    date_ajout = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Paiement de {self.user.username}"



from django.db import models

class Counter(models.Model):
    count = models.PositiveIntegerField(default=81)  # Initialise à 1

    def __str__(self):
        return str(self.count)


from django.db import models

class Decompte(models.Model):
    count = models.PositiveIntegerField(default=46800)  # Initialisé à 46800

    def decrement(self):
        if self.count > 0:
            self.count -= 1
            self.save()

    def __str__(self):
        return str(self.count)
