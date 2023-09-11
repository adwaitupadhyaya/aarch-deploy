from django.db import models

# Create your models here


class PropertyModel(models.Model):
    property_name = models.CharField(
        max_length=50, null=False, blank=False)
    property_area = models.IntegerField(null=False, blank=False)
    property_dimensions = models.CharField(
        max_length=50, null=False, blank=False)
    property_image = models.ImageField()
    property_description = models.TextField()

    def __str__(self):
        return self.property_name
