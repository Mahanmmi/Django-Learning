from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloWorldAPIView(APIView):

    serializerClass = serializers.HelloSerializer

    def get(self, request, format=None):
        what_is_this = [
            'Hello there',
            'General Kenobi',
            'You are shorter',
            'Than I expected General Grievous'
        ]

        return Response({'message': 'Hi!', 'wit': what_is_this})

    def post(self, request):
        serializer = self.serializerClass(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            return Response({'message': f'Hello there {name}'})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})
    