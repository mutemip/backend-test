from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    profile_picture = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'full_name', 'profile_picture')

    def get_full_name(self, obj):
        social = obj.social_auth.get(provider='google-oauth2')
        return social.extra_data.get('name', '')

    def get_profile_picture(self, obj):
        social = obj.social_auth.get(provider='google-oauth2')
        return social.extra_data.get('picture', '')
