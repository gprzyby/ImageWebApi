from rest_framework.permissions import BasePermission, DjangoObjectPermissions
from rest_framework.request import Request


def _check_if_authenticated(user) -> bool:
    return user and user.is_authenticated


class IsAuthenticatedOrPost(BasePermission):

    def has_permission(self, request: Request, view):
        return request.method == 'POST' or _check_if_authenticated(request.user)


class IsModelOwner(DjangoObjectPermissions):

    additional_perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'HEAD': ['%(app_label)s.view_%(model_name)s'],
    }

    def __init__(self):
        super().__init__()
        self.perms_map = {**self.perms_map, **self.additional_perms_map}

    def has_permission(self, request, view):
        return _check_if_authenticated(request.user)


