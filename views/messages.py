__author__ = 'sriram'

import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utlis import timezone

from accounts.models import UserProfile
from models import Message
from serializer import MessageSerializer

logger = logging.get_logger("Message API")


class MessageAPI(APIView):

    def get(self, request):

        try:
            logger.info("Getting messages for user: %s" % request.user)
            user = UserProfile.objects.get(user_id=request.user.id)
            messages = Message.objects.filter(received_by=request.user).\
                filter(sent_at__gt=user.last_seen_at)
            messages_serializer = MessageSerializer(messages, many=True)
            response = messages_serializer.data
            user.last_seen_at = timezone.now()
            user.save()
            Message.objects.filter(id__in=messages.values('id')).\
                update(received_at=timezone.now())
            Message.objects.filter(id__in=messages.values('id')).\
                update(is_viewed=True)
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error("Exception: %s" % e)
            response = {"msg": "User not found"}
            return Response(response, status=status.HTTP_404_NOT_FOUND)
