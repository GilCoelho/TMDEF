from django.urls import path
from . import views

urlpatterns = [
    path("form/", views.evaluation_form, name="formFiller"),
    path("feedback/", views.feedback, name="createData"),
]
