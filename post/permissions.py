from allauth.account.models import EmailAddress
from rest_framework import permissions


class IsAuthenticatedVerified(permissions.BasePermission):

    def has_permission(self, request, view):
        email = EmailAddress.objects.filter(email=request.user.email)
        verified = [e.verified for e in email]

        if request.user.is_staff:
            return bool(request.user and request.user.is_staff)

        return bool(request.user and request.user.is_authenticated and
                     verified[0])
