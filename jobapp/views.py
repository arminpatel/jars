from rest_framework.generics import ListCreateAPIView

from jobapp.models import Application
from jobapp.serializers import ApplicationSerializer


class ListCreateApplicationView(ListCreateAPIView):
    """View to list and create application"""
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
