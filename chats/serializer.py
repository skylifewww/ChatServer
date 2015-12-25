__author__ = 'sriram'

from rest_framework import routers, serializers, viewsets
from models import Message


# Serializers define the API representation.
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('sent_by',
                  'message',
                  'sent_at',
                  'received_by')
