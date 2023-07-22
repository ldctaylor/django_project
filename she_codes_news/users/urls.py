# users/urls.py
from django.urls import path
from .views import CreateAccountView
from .views import ViewAccountProfile

app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    path('account-profile/', ViewAccountProfile.as_view(), name='viewAccount'),
]