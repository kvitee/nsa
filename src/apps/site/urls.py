from django.urls import path

from .views import StartPageView


urlpatterns = [
    path("", StartPageView.as_view()),
]
