from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
import requests

class GoogleOAuth2Authentication(BaseAuthentication):
    def authenticate(self, request):
        authorization_header = request.headers.get('Authorization')
        if not authorization_header:
            return None
        
        try:
            token_type, token = authorization_header.split()
        except ValueError:
            raise AuthenticationFailed('Invalid token header. No credentials provided.')
        
        if token_type != 'Bearer':
            raise AuthenticationFailed('Authorization header must use Bearer token.')

        # Validate the access token with Google
        response = requests.get(
            'https://www.googleapis.com/oauth2/v3/tokeninfo',
            params={'access_token': token}
        )
        
        if response.status_code != 200:
            raise AuthenticationFailed('Invalid or expired token.')
        
        # Get the token's user info
        token_data = response.json()
        
        return (token_data, None)
