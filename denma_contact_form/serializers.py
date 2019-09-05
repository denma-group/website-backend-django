import logging
from rest_framework import serializers
from denma_contact_form import models
from denma_subscribe_form.models import SubscribedUser

import logging
logger = logging.getLogger(__name__)


class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ContactForm
        fields = ('id', 'email', 'name', 'message', 'created_on', 'subscribe_news')

    def create(self, validated_data):
        logger.info('Information incoming!')
        subscribed_user = None
        logging.debug(('subscribe_news', self.field_name('subscribe_news')))
        logger.info("self.field_name('subscribe_news'): ", self.field_name('subscribe_news'))
        if self.field_name('subscribe_news'):
            email = self.field_name('email')
            name = self.field_name('name')
            subscribed_user = SubscribedUser.objects.create(email=email, name=name)
            subscribed_user.save()
        contact_form = models.ContactForm(**validated_data, subscribed_user=subscribed_user)
        return contact_form
