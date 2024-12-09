from django.urls import path
from . import views

urlpatterns = [
    path("form/", views.evaluation_form, name="formFiller"),
    path("feedback/", views.feedback, name="createData"),
    path("thanks_for_feedback/", views.thanks_for_feedback, name="thanksForFeedBack"),
]
