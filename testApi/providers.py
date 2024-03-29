from dj_rest_auth.registration.views import SocialLoginView
from dj_rest_auth.registration.views import SocialConnectView

from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter



class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter

class GoogleConnect(SocialConnectView):
    adapter_class = GoogleOAuth2Adapter
