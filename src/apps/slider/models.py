from django.db import models

from filer.fields.image import FilerImageField


class Slider(models.Model):
    name = models.CharField(
        verbose_name="название",
        max_length=255,
    )

    slug = models.SlugField(
        verbose_name="короткое уникальное название (slug)",
        max_length=255,
        unique=True,
        default="start_page_slider",
    )

    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = "sliders"
        verbose_name = "слайдер"
        verbose_name_plural = "слайдеры"


class SliderEntry(models.Model):
    slider = models.ForeignKey(
        to=Slider,
        on_delete=models.CASCADE,
        related_name="entry_slider",
        verbose_name = "слайдер",
    )

    number = models.PositiveSmallIntegerField(
        verbose_name="порядок",
        default=0,
    )

    image = FilerImageField(
        on_delete=models.CASCADE,
        related_name="entry_image",
        verbose_name="картинка"
    )

    def __str__(self):
        return "Элемент слайдера \"{}\" с картинкой {}".format(
            self.slider,
            self.image,
        )

    class Meta:
        db_table = "slider_entries"
        verbose_name = "элемент слайдера"
        verbose_name_plural = "элементы слайдеров"
        ordering = ("number", )
