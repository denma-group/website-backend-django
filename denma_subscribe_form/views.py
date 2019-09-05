from rest_framework.viewsets import ModelViewSet
# Local
from denma_subscribe_form import serializers, models


class SubscribedUserViewSet(ModelViewSet):
    """Contact form ViewSet to handle submissions or updates"""
    serializer_class = serializers.SubscribedUserSerializer
    queryset = models.SubscribedUser.objects.all()

    def perform_create(self, serializer):
        """Sets subscribe_news to True by default when calling POST create"""
        serializer.save(subscribe_news=True)

