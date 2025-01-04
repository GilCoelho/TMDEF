from django.db import models


class SpeechToEval(models.Model):
    speaker = models.CharField(max_length=255)
    speaker_email = models.CharField(max_length=255)
    speech_name = models.CharField(max_length=255)
    pathway_challenge = models.CharField(max_length=255)
    feedback_form = models.CharField(max_length=255)  # models.IntegerChoices()


class FeedBackFormsList(models.Model):
    value = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
