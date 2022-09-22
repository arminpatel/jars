from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('applications/', include('jobapp.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
