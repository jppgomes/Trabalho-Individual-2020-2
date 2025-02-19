"""
api mode.

model objects.
"""


from django.db import models


class Task(models.Model):
    """
    Model Task.

    model task object.
    """

    title = models.CharField("Title", max_length=240)
    description = models.CharField("Title", max_length=240)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        """
        str.

        convert so str.
        """
        return self.name
