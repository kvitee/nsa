from django.views.generic import TemplateView

from apps.slider.models import SliderEntry


class StartPageView(TemplateView):
    template_name = "start_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["slider_entries"] = SliderEntry.objects.all().filter(
            slider__slug="start_page_slider"
        )

        return context
