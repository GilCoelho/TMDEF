from django.db import models

class EvaluationForm(models.Model):
  first_answer = models.CharField(max_length=255)
  second_answer = models.CharField(max_length=255)
  third_answer = models.CharField(max_length=255)
