from django.contrib import admin

from apps.slider.models import Slider, SliderEntry


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    pass


@admin.register(SliderEntry)
class SliderEntryAdmin(admin.ModelAdmin):
    pass
