from rest_framework import serializers
from denma_contact_form import models


class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ContactForm
        fields = ('id', 'email', 'name', 'message', 'created_on', 'subscribe_news')
