from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode

from adminsortable2.admin import (
    SortableAdminBase,
    SortableAdminMixin,
    SortableStackedInline,
)
from easy_thumbnails.files import get_thumbnailer

from .models import Slider, SliderEntry


class SliderEntryStackedInline(SortableStackedInline):
    model = SliderEntry
    extra = 0


@admin.register(Slider)
class SliderAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ("name", "slug", "get_entries_url")

    inlines = (SliderEntryStackedInline, )

    def get_entries_url(self, slider: Slider):
        url = (
            reverse("admin:slider_sliderentry_changelist")
            + "?"
            + urlencode({"slider__id": f"{slider.id}"})
        )

        return format_html("<a href={}>Элементы</a>", url)

    get_entries_url.short_description = "Ссылка на список элементов"


@admin.register(SliderEntry)
class SliderEntryAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ("number", "get_image_html", "slider")

    def get_image_html(self, slider_entry: SliderEntry):
        thumbnail_url = get_thumbnailer(
            slider_entry.image
        ).get_thumbnail({
            "size": (40, 40),
            "crop": True,
        }).url

        return format_html("<img src={} />", thumbnail_url)

    get_image_html.short_description = "Картинка"
