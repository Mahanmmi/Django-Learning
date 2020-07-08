from rest_framework import serializers

from profiles_api import models


class HelloSerializer(serializers.Serializer):
    """:|"""
    name = serializers.CharField(max_length=10)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'age', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        user = models.UserProfile.objects.create_user(
            email=validated_data.get('email'),
            name=validated_data.get('name'),
            age=validated_data.get('age'),
            password=validated_data.get('password')
        )
        return user
