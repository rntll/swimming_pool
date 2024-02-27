from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('schedule',views.schedule, name='schedule'),
    path('instructors/', views.instructors_view, name='instructors'),
    path('accounts/', include('accounts.urls')),
]