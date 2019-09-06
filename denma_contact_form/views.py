from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
# Local
from denma_contact_form import serializers, models
from denma_subscribe_form.models import SubscribedUser


class ContactFormViewSet(ModelViewSet):
    """Contact form ViewSet to handle submissions or updates"""
    serializer_class = serializers.ContactFormSerializer
    queryset = models.ContactForm.objects.all()

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
            subscribe_news = serializer.validated_data.get('subscribe_news')
            if subscribe_news:
                SubscribedUser.objects.get_or_create(
                    name=serializer.validated_data.get('name'),
                    email=serializer.validated_data.get('email'),
                    subscribe_news=True,
                )
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

