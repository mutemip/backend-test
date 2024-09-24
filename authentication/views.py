from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from social_django.models import UserSocialAuth
import requests

def google_login(request):
    return redirect('/oauth/login/google-oauth2/')


class UserProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]  # Require the user to be authenticated
    
    def get(self, request, *args, **kwargs):
        user = request.user  # The currently logged-in user
        
        # Fetch the user's profile info
        user_profile = {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
        }

        # Try to get the Google OAuth2 access token for the user, ordering by the most recent
        social_auths = UserSocialAuth.objects.filter(user=user, provider='google-oauth2').order_by('-id')
        
        if social_auths.exists():
            social_auth = social_auths.first()  # Get the most recent association
            access_token = social_auth.extra_data.get('access_token')

            return Response({
                "user_profile": user_profile,
                "google_oauth2": {
                    "access_token": access_token,
                }
            })
        
        return Response({
            "error": "Google OAuth2 token not found for this user."
        }, status=404)
