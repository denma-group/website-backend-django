from django.db import models


class ContactForm(models.Model):
    """Contact form model"""
    email = models.EmailField(max_length=255, null=False)
    name = models.CharField(max_length=255, null=False)
    message = models.CharField(max_length=25500, null=False)
    created_on = models.DateTimeField(auto_now_add=True)
    subscribe_news = models.BooleanField(null=False, default=False)
    subscribed_user = models.ForeignKey(
        'denma_subscribe_form.SubscribedUser',
        on_delete=models.SET_NULL,
        null=True,
        related_name='subscribed_user',
        editable=False
    )

    def __str__(self):
        """Return the model's email as a string"""
        return self.email
