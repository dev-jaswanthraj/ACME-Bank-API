from django.conf.urls import url
from acme_bank_api.core_banking_system import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^$', views.api_root, name='list-routes'),
    url(r'^accounts/create/', views.AccountCreate.as_view(), name='account-create'),
    url(r'^accounts/$', views.AccountList.as_view(), name='account-list'),
    url(r'^accounts/(?P<pk>[0-9]+)/$', views.AccountDetail.as_view(), name='account-detail'),
    url(r'^transactions/create/', views.TransactionCreate.as_view(), name='trans-create'),
    url(r'^transactions/$', views.TransactionList.as_view(), name='trans-list'),
]

urlpatterns += format_suffix_patterns(urlpatterns)
