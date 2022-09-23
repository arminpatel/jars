from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from django.db import models

User = get_user_model()


class Application(models.Model):

    STATUS = (
        ('IR', 'In Review'),
        ('RJ', 'Rejected'),
        ('AC', 'Accepted'),
        )

    applicant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')
    opening = models.CharField(max_length=25)     # should be a foreign key
    status = models.CharField(max_length=2, choices=STATUS, default='IR')
    description = models.TextField(null=True)
    resume = models.FileField(upload_to='upload', blank=True, validators=[
                              FileExtensionValidator(allowed_extensions=['pdf'])])
