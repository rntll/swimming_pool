from django.contrib.auth.decorators import user_passes_test

def superuser_required(view_func):
    decorated_view_func = user_passes_test(lambda user: user.is_superuser)
    return decorated_view_func(view_func)

def user_required(view_func):
    decorated_view_func = user_passes_test(lambda user: not user.is_superuser)
    return decorated_view_func(view_func)


