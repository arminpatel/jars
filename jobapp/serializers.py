from rest_framework import serializers

from jobapp.models import Application


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['id', 'applicant', 'opening', 'status', 'description', 'resume']
        extra_kwargs = {
            'id': {'read_only': True},
        }
