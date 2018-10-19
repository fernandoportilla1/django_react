from django.core.exceptions import PermissionDenied


class AdminDeniedMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_superuser:
            raise PermissionDenied
        response = self.get_response(request)

        return response
