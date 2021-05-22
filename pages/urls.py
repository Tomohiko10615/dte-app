from django.urls import path

from .views import HomePageView

from . import views

urlpatterns = [
    path('', HomePageView.as_view(), name = "home"),
    path("fetch", views.fetch, name = "fetch"),
    path("serve",views.serve, name="serve"),
]