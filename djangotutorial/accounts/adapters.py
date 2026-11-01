from urllib.parse import urlencode

from django.conf import settings
from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site

from allauth.account.adapter import DefaultAccountAdapter

class CustomAccountAdapter(DefaultAccountAdapter):

    def get_logout_redirect_url(self, request):

        return_url = request.build_absolute_uri(
            reverse("home")
        )

        client_id = settings.SOCIALACCOUNT_PROVIDERS["openid_connect"]["APPS"][0]['client_id']
        server_url = settings.SOCIALACCOUNT_PROVIDERS["openid_connect"]["APPS"][0]['settings']['server_url']

        params = {
            "client_id": client_id,
            "post_logout_redirect_uri": return_url,
        }

        return (
            f"{server_url}/oidc/logout?"
            f"{urlencode(params)}"
        )
