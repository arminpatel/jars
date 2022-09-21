from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Application(models.Model):
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    opening = models.CharField(max_length=25)     # should be a foreign key
    selected = models.BooleanField(default=False)
    description = models.TextField(null=True)
