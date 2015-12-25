__author__ = 'sriram'

from rest_framework import routers, serializers, viewsets
from accounts.models import UserProfile


# Serializers define the API representation.
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id',
                  'username',
                  'email',
                  'date_joined',
                  'last_seen_at')