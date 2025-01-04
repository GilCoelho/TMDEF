from django.urls import path
from . import views

urlpatterns = [
    path("", views.form_selector, name="speechSelector"),
    path("add_speech/", views.add_speech, name="addSpeech"),
]
