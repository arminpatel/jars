from rest_framework import permissions
from rest_framework.generics import (GenericAPIView, ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.mixins import UpdateModelMixin

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


class PartialUpdateStatusApplicationView(GenericAPIView, UpdateModelMixin):
    """Partial update selected status"""
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
