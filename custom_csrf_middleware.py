from django.middleware.csrf import CsrfViewMiddleware


class CustomCsrfViewMiddleware(CsrfViewMiddleware):
    """
    Skip CSRF checks for requests from localhost.
    For development only.

    Usage:
        1. remove "django.middleware.csrf.CsrfViewMiddleware" from MIDDLEWARES
        2. add 'app_name.middleware.CsrfViewMiddlewareMutated'

    * MIDDLEWARES variable is located at `project_name/project_name/settings.py`
    """
    def process_view(self, request, view_func, view_args, view_kwargs):
        """ Returns None for localhost to skip CSRF check """
        if request.META['REMOTE_ADDR'] in ['127.0.0.1', '::1']:
            return None
        return super().process_view(request, view_func, view_args, view_kwargs)
