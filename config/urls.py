from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

urlpatterns = [

    url(settings.ADMIN_URL, admin.site.urls),
    url(r'^api/core_banking_system/', include('acme_bank_api.core_banking_system.urls')),
    url(r'^api/users/', include('acme_bank_api.users.urls')),

]

schema_view = get_schema_view(
    openapi.Info(
        title="ACME Bank Corp.",
        default_version='v1',
        description="Owned by Vinayak",
    ),
    validators=['flex', 'ssv'],
    public=True,
)

urlpatterns += [
    url(r'^docs/swagger(?P<format>.json|.yaml)$', schema_view.without_ui(cache_timeout=None),name='schema-json'),
    url(r'^docs/swagger/$', schema_view.with_ui('swagger', cache_timeout=None),name='schema-swagger-ui'),
    url(r'^docs/redoc/$', schema_view.with_ui('redoc', cache_timeout=None), name='schema-redoc'),
]

if settings.DEBUG:
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns = [
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ] + urlpatterns
