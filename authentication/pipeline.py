from social_core.exceptions import AuthAlreadyAssociated
from social_django.models import UserSocialAuth

def handle_existing_association(backend, uid, user=None, *args, **kwargs):
    try:
        # Find the social association for the current provider and uid
        existing_user_social_auth = UserSocialAuth.objects.get(provider=backend.name, uid=uid)
        
        # If the current user and the existing user associated with this social auth are different
        if user and existing_user_social_auth.user != user:
            # Unlink the previous association and re-link it to the new user
            existing_user_social_auth.delete()  # Unlink the social account
            return {
                'user': user  # Associate with the current user
            }
        else:
            # If the social account is already linked to the same user, do nothing
            return {
                'user': existing_user_social_auth.user
            }
    except UserSocialAuth.DoesNotExist:
        # If no existing association is found, continue with the process
        return None
