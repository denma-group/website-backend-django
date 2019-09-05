from rest_framework.viewsets import ModelViewSet
# Local
from denma_contact_form import serializers, models


class ContactFormViewSet(ModelViewSet):
    """Contact form ViewSet to handle submissions or updates"""
    serializer_class = serializers.ContactFormSerializer
    queryset = models.ContactForm.objects.all()

