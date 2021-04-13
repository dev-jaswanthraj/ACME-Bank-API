from django.conf.urls import url
from rest_framework.authtoken import views as auth_view
from acme_bank_api.users import views

urlpatterns = [
    url(r'signup/', views.UserCreate.as_view(), name='user-create'),
    url(r'signin/', auth_view.obtain_auth_token, name='account_login')
]
