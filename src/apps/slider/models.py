from django.db import models

from filer.fields.image import FilerImageField


class Slider(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = "sliders"


class SliderEntry(models.Model):
    slider = models.ForeignKey(
        to=Slider,
        on_delete=models.CASCADE,
    )

    number = models.PositiveSmallIntegerField()
    image = FilerImageField(
        related_name="entry_image",
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = "slider_entries"
        ordering = ["number"]
