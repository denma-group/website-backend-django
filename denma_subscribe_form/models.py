from django.db import models


class SubscribedUser(models.Model):
    """Subscribed user model"""
    email = models.EmailField(max_length=255, null=False, unique=True)
    name = models.CharField(max_length=255, null=False)
    created_on = models.DateTimeField(auto_now_add=True)
    subscribe_news = models.BooleanField(null=False, default=True)

    def __str__(self):
        """Return the model's email as a string"""
        return self.email
