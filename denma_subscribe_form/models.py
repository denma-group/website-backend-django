from django.db import models


class SubscribeFormManager(models.manager.BaseManager):
    """Manager for subscribe forms"""
    def create_form(self, email, name):
        """Create a new form"""
        if not email:
            raise ValueError("Subscriptions must have an email address.")
        email = self.normalize_email(email)
        """Overwriting the default model"""
        form = self.model(email=email, name=name)
        form.save(using=self.db)
        return form
