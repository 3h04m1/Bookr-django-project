from django.db import models


class Publisher(models.Model):
    """A company that publishes books"""

    name = models.CharField(max_length=50, help_text="The name of the publisher")
    website = models.URLField(help_text="the publisher's website")
    email = models.EmailField(help_text="publisher's email")

    def __str__(self):
        return self.name

# Create your models here.
