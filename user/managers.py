from django.contrib.auth.base_user import BaseUserManager

class RecuritManager(BaseUserManager):
    def create_user(self, code, password, *args, **kwargs):
        if not code:
            raise ValueError("code is not provided.")
        
        doctor_account = self.model(code=code, password=password, *args, **kwargs)
        doctor_account.set_password(password)
        doctor_account.save()

        return doctor_account
    
    def create_superuser(self, code, **kwargs):
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_active", True)    
        kwargs.setdefault("is_superuser", True)

        admin_account = self.create_user(code, **kwargs)
        return admin_account