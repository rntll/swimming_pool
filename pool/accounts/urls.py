from django.urls import path
from .views import signup, login_view, profile_view, admin_panel_view,add_info, add_comment, review_page
from django.conf import settings
from django.conf.urls.static import static

app_name = 'accounts'

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('profile/', profile_view, name='profile'),
    path('add_info/',add_info, name='add_info'),
    path('admin_panel/',admin_panel_view, name='admin_panel'),
    path('reviews/', review_page, name='review_page'),
    path('reviews/<int:review_id>/add_comment/', add_comment, name='add_comment'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
