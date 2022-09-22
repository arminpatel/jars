from rest_framework import permissions
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)

from jobapp.models import Application
from jobapp.serializers import ApplicationSerializer


class ListCreateApplicationView(ListCreateAPIView):
    """View to list and create application"""
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = (permissions.IsAuthenticated,)


class RetrieveUpdateDestroyApplicationView(RetrieveUpdateDestroyAPIView):
    """View to retrieve, update and destroy application"""
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = (permissions.IsAuthenticated,)
