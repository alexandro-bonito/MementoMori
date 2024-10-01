from django.contrib.auth.backends import BaseBackend
from .models import CustomUser

class WhatsAppAuthBackend(BaseBackend):
    def authenticate(self, request, numero_whatsapp=None, date_naissance=None):
        try:
            # Ne pas authentifier les superadmins avec ce backend
            user = CustomUser.objects.get(numero_whatsapp=numero_whatsapp, date_naissance=date_naissance)
            if user.is_superuser:
                return None
            return user
        except CustomUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None
