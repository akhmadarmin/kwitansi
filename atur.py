from django.http import HttpResponseForbidden

def group_required(*group_names):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated:
                if bool(request.user.groups.filter(name__in=group_names)) or request.user.is_superuser:
                    return view_func(request, *args, **kwargs)
            return HttpResponseForbidden("Anda tidak memiliki izin untuk akses halaman ini")
        return _wrapped_view
    return decorator