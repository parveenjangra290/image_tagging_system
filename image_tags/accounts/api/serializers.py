"""
    User login/profile serializers.
"""
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from datetime import timedelta
from django.utils import timezone
from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class UserLoginSerializer(serializers.ModelSerializer):
    """
    User login serializers
    """
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)

    class Meta(object):
        """ Meta information """
        model = User
        fields = ('id', 'username', 'password')

    def validate(self, attrs):
        """
            Validate User details.
            :param attrs: Ordered Dictionary containing username and password.
            :return : attrs
        """
        username = attrs.get('username')
        password = attrs.get('password')
        auth_user = authenticate(self.context['request'], username=username, password=password)
        if not auth_user:
            raise serializers.ValidationError("Invalid Username/Password")
        existing_token = Token.objects.filter(user=auth_user)
        if not existing_token:
            Token.objects.create(user=auth_user)
        else:
            last_token_datetime = existing_token[0].created
            if timezone.now() > last_token_datetime + timedelta(minutes=settings.TOKEN_EXPIRY_TIME):
                existing_token[0].delete()
                Token.objects.create(user=auth_user)
        attrs.update({'user': auth_user})
        return attrs

    def login(self, **kwargs):
        return self.validated_data.get('user')


class UserProfileSerializer(serializers.ModelSerializer):
    """
        User Profile Serializer
    """
    auth_token = serializers.SerializerMethodField(read_only=True)

    class Meta(object):
        """ Meta information """
        model = User
        fields = ('id', 'username', 'email', 'auth_token')

    @staticmethod
    def get_auth_token(obj):
        try:
            return str(obj.auth_token)
        except:
            return '0'
