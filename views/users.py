__author__ = 'sriram'

import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from accounts.models import UserProfile
from accounts.serializer import UserProfileSerializer

logger = logging.get_logger('UserProfileAPI')


class UserProfileAPI(APIView):

    def post(self, request, format=None):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        user = request.data.get('username', None)
        if user is not None:
            try:
                logger.info('Deleting user: %s' % user)
                user = UserProfile.objects.filter(username=user)
                user.delete()
                return Response({"msg": 'User Deleted Successfully'}, status=status.HTTP_200_OK)
            except Exception as e:
                logger.error('Error: %s' % e)
                return Response({"msg": 'User Not found'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"msg": 'Bad request'}, status=status.HTTP_400_BAD_REQUEST)
