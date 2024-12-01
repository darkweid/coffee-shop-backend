import uuid

from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def save(self, **kwargs):
        user = super().save(**kwargs)
        user.verification_token = str(uuid.uuid4())
        user.save()

        # ToDo: use send email in production
        # send_mail(
        #     'Verify your account',
        #     f'Your verification token is {user.verification_token}',
        #     'noreply@example.com',
        #     [user.email],
        #     fail_silently=False,
        # )
        print(f'\nYour verification token is {user.verification_token}\n')
        return user


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'is_active')
