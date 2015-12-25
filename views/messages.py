__author__ = 'sriram'

import logging
import sys, traceback
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from rest_framework import viewsets
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from accounts.models import UserProfile
from chats.models import Message
from chats.serializer import MessageSerializer

logger = logging.getLogger("Message API")


class PaginatedMessageSerializer(object):
    def __init__(self, messages, request, num):
        """
        Pagination for the messages. Default no of messages per page 10.
        :param messages:
        :param request:
        :param num:
        :return:
        """
        paginator = Paginator(messages, num)
        page = request.query_params.get('page')
        try:
            messages = paginator.page(page)
        except PageNotAnInteger:
            messages = paginator.page(1)
        except EmptyPage:
            messages = paginator.page(paginator.num_pages)
        count = paginator.count

        previous = None if not messages.has_previous() else messages.previous_page_number()
        next = None if not messages.has_next() else messages.next_page_number()
        serializer = MessageSerializer(messages, many=True)
        self.data = {
            'meta': {
                'count': count,
                'took': len(serializer.data),
                'current_page': page,
                'previous': previous,
                'next': next
            },
            'messages': serializer.data
        }


class MessageAPI(APIView):

    def get(self, request):
        """
        Returns latest messages for the user. Messages will be returned in the order of latest at top.
        :param request:
        :return: messages as response
        """
        try:
            logger.info("Getting messages for user: %s" % request.user)
            user = UserProfile.objects.get(id=request.user.id)
            messages = Message.objects.filter(received_by=request.user).\
                filter(sent_at__gt=user.last_seen_at).order_by('-id')
            messages_serializer = PaginatedMessageSerializer(messages, request, 10)
            response = messages_serializer.data
            messages_ids = messages.values_list('id', flat=True)
            print "Messages: %s" % messages_ids
            user.last_seen_at = timezone.now()
            user.save()

            if response:
                Message.objects.mark_viewed(messages_ids)
                return Response(response, status=status.HTTP_200_OK)
            else:
                response = {'msg': 'No new message'}
                return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            traceback.print_exc(e)
            logger.error("Exception: %s" % e)
            response = {"msg": "User not found"}
            return Response(response, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        """
        Send message to the user.
        :param request:
        :return: response with status
        """
        try:
            id = request.data.get('user_id', None)
            user = UserProfile.objects.get(id=id)
            logger.info("Sending Messages to user: %s" % user)
        except Exception as e:
            traceback.print_exc(e)
            logger.error("Exception: %s" % e)
            response = {'msg': "Message can't be sent. User doesn't exists"}
            return Response(response, status=status.HTTP_404_NOT_FOUND)

        msg = request.data.get('message')

        if not msg:
            response = {'msg': 'Bad request. Message is null'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        message = Message(sent_by=request.user,
                          received_by=user,
                          message=msg)
        message.save()
        response = {'msg': 'Message sent successfully'}
        return Response(response, status=status.HTTP_200_OK)