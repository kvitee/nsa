from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin

from apps.slider.models import Slider, SliderEntry


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    pass


@admin.register(SliderEntry)
class SliderEntryAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass
