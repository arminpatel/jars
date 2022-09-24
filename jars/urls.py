from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view

schema_view = swagger_get_schema_view(
    openapi.Info(
        title='Application API',
        default_version='1.0.0',
        description='API documentation for application',
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('applications/', include('jobapp.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('swagger/schema/', schema_view.with_ui('swagger', cache_timeout=0),
         name='swagger-schema'),

]
