from django.urls import path
from userprofile import views as user_views

urlpatterns = [
    path('userprofile/', user_views.profile, name='profile'),
]
