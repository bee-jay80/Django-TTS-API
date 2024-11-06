from django.urls import path
from .views import AudioCreateView #, AudioDeleteAllView

urlpatterns = [
    path("create/", AudioCreateView.as_view(), name="create"),
]