__author__ = 'sriram'

import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from accounts.models import UserProfile
from accounts.serializer import UserProfileSerializer

logger = logging.getLogger('UserProfileAPI')


class UserProfileAPI(APIView):

    def get(self, request):
        user_id = request.query_params.get('user_id', None)
        try:
            user = UserProfile.objects.get(id=user_id)
            serializer = UserProfileSerializer(user)    
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error("Unable to find user id: %s" % e)
            response = {'msg': "User doesn't exists"}
            return Response(response, status=status.HTTP_404_NOT_FOUND)

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
