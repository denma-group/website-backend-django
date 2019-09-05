from rest_framework import serializers

# Local
from denma_subscribe_form import models


class SubscribedUserSerializer(serializers.ModelSerializer):
    """Serializes contact forms"""

    class Meta:
        model = models.SubscribedUser
        fields = ('id', 'email', 'name', 'created_on', 'subscribe_news')
