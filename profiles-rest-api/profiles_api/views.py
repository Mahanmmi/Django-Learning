from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, filters
from rest_framework.authentication import TokenAuthentication

from profiles_api import serializers, models, permissions


class HelloWorldAPIView(APIView):
    serializer_class = serializers.HelloSerializer

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


class HelloViewSet(viewsets.ViewSet):
    """For view set thing"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return list of all"""
        a_viewset = [
            'Hello there',
            'General Kenobi',
            'You are shorter',
            'Than I expected General Grievous',
        ]

        return Response({'message': 'hmmm', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new hello message."""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""
        return Response({'http_method': f'GET {pk}'})

    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'http_method': f'PUT {pk}'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""
        return Response({'http_method': f'PATCH {pk}'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({'http_method': f'DELETE {pk}'})


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email', 'age')
