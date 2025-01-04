from datetime import datetime

from django.db import models

from Forms.FormSelector.models import SpeechToEval

EMPTY_COMMENT = "No Comment"


class EvaluationDBTable(models.Model):
    # Date of the moment for the creation of the evaluation
    fill_date = models.DateTimeField(auto_created=True, auto_now=True)

    # Feed-back data
    first_answer = models.CharField(max_length=255)
    second_answer = models.CharField(max_length=255)
    third_answer = models.CharField(max_length=255)

    evaluator_name = models.CharField(max_length=255)

    criteria_resp_1 = models.IntegerField(default=0)
    criteria_resp_1_comment = models.CharField(max_length=255, default=EMPTY_COMMENT)

    criteria_resp_2 = models.IntegerField(default=0)
    criteria_resp_2_comment = models.CharField(max_length=255, default=EMPTY_COMMENT)

    criteria_resp_3 = models.IntegerField(default=0)
    criteria_resp_3_comment = models.CharField(max_length=255, default=EMPTY_COMMENT)

    criteria_resp_4 = models.IntegerField(default=0)
    criteria_resp_4_comment = models.CharField(max_length=255, default=EMPTY_COMMENT)

    criteria_resp_5 = models.IntegerField(default=0)
    criteria_resp_5_comment = models.CharField(max_length=255, default=EMPTY_COMMENT)

    criteria_resp_6 = models.IntegerField(default=0)
    criteria_resp_6_comment = models.CharField(max_length=255, default=EMPTY_COMMENT)

    criteria_resp_7 = models.IntegerField(default=0)
    criteria_resp_7_comment = models.CharField(max_length=255, default=EMPTY_COMMENT)

    criteria_resp_8 = models.IntegerField(default=0)
    criteria_resp_8_comment = models.CharField(max_length=255, default=EMPTY_COMMENT)

    criteria_resp_9 = models.IntegerField(default=0)
    criteria_resp_9_comment = models.CharField(max_length=255, default=EMPTY_COMMENT)

    criteria_resp_10 = models.IntegerField(default=0)
    criteria_resp_10_comment = models.CharField(max_length=255, default=EMPTY_COMMENT)

    criteria_resp_11 = models.IntegerField(default=0)
    criteria_resp_11_comment = models.CharField(max_length=255, default=EMPTY_COMMENT)

    criteria_resp_12 = models.IntegerField(default=0)
    criteria_resp_12_comment = models.CharField(max_length=255, default=EMPTY_COMMENT)

    # ID of the Speech present in the SpeechToEval table
    speech_evaluated = models.ForeignKey(SpeechToEval, on_delete=models.CASCADE)

    # Bool to indicate if the mail with this answers was send
    mail_sended = models.BooleanField(default=False)
