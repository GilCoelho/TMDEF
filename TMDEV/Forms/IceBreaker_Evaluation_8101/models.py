from datetime import datetime

from django.db import models

from Forms.Form_Selector.models import SpeechToEval


class EvaluationForm(models.Model):
    # Date of the moment for the creation of the evaluation
    fill_date = models.DateField(auto_created=True, default=datetime.now)

    # Feed-back data
    first_answer = models.CharField(max_length=255)
    second_answer = models.CharField(max_length=255)
    third_answer = models.CharField(max_length=255)

    # ID of the Speech present in the SpeechToEval table
    speech_evaluated = models.ForeignKey(SpeechToEval, on_delete=models.CASCADE)

    # Bool to indicate if the mail with this answers was send
    mail_sended = models.BooleanField(default=False)
