from rest_framework.permissions import BasePermission
from rest_framework.request import Request


def _check_if_authenticated(user) -> bool:
    return user and user.is_authenticated


class IsAuthenticatedOrPost(BasePermission):

    def has_permission(self, request: Request, view):
        return request.method == 'POST' or _check_if_authenticated(request.user)