from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from abc import ABC

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password',)

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, required=True, write_only=True)
    password_confirmation = serializers.CharField(min_length=8, required=True, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password', 'password_confirmation', 'email')

    def validate(self, attrs):
        password2 = attrs.pop('password_confirmation')
        if password2 != attrs['password']:
            raise serializers.ValidationError(
                'Passwords didn\'t match')
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user



class ActivationSerializer(serializers.Serializer):
    code = serializers.CharField(required=True, max_length=255)
    default_error_messages = {
        'bad_code': _('Code is expired or invalid!')
    }

    def validate(self, attrs):
        self.code = attrs['code']
        return attrs

    def save(self, **kwargs):
        try:
            user = User.objects.get(activation_code=self.code)
            user.is_active = True
            user.activation_code = ''
            user.save()
        except User.DoesNotExist:
            self.fail('bad_code')