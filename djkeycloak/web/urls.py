from django.contrib.auth.decorators import login_required
from django.urls import path, include
from .views import IndexView


urlpatterns = [
    path("", IndexView.as_view(), name="web_index_view"),
]
