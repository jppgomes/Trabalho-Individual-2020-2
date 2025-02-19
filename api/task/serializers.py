"""

Django serializer objects.

Serialize task

"""

from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """
    Django settings for api project.

    Generated by 'django-admin startproject' using Django 3.2.
    """

    class Meta:
        """
        Django settings for api project.

        Generated by 'django-admin startproject' using Django 3.2.
        """

        model = Task
        fields = ['pk', 'title', 'description', 'created']
