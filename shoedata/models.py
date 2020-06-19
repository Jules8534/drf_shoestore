from django.db import models

"""Joe is considered himself to be a "Code monkey with a desire to leave the world better than he found it."""
from django.contrib.auth.models import User


User = User



class Manufacturer(models.Model):
    name = models.CharField(max_length=50, unique=True)
    website = models.URLField()

    def __str__(self):
        return self.name


class ShoeType(models.Model):
    style = models.CharField(max_length=50)

    def __str__(self):
        return self.style


class ShoeColor(models.Model):
    RED = 'R'
    ORANGE = 'O'
    YELLOW = 'Y'
    GREEN = 'G'
    BLUE = 'B'
    INDIGO = 'I'
    VIOLET = 'V'
    WHITE = 'W'
    BLACK = 'B'

    COLOR_CHOICES = [
        (RED, "Red"),
        (ORANGE, "Orange"),
        (YELLOW, "Yellow"),
        (GREEN, "Green"),
        (BLUE, "Blue"),
        (INDIGO, "Indigo"),
        (VIOLET, "Violet"),
        (WHITE, "White"),
        (BLACK, "Black"),
    ]

    color_name = models.CharField(
        max_length=1,
        choices=COLOR_CHOICES,
    )

    def __str__(self):
        return self.color_name


class Shoe(models.Model):
    size = models.IntegerField(help_text="No half sizes available.")
    brand_name = models.CharField(max_length=50)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    color = models.ForeignKey(ShoeColor, on_delete=models.CASCADE)
    material = models.CharField(max_length=50)
    shoe_type = models.ForeignKey(ShoeType, on_delete=models.CASCADE)
    fasten_type = models.CharField(max_length=50)

    def __str__(self):
        description = "_".join(
            [self.brand_name, self.color.color_name, str(self.size)])
        return description
