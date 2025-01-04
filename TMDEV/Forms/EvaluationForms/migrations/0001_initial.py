# Generated by Django 4.2.16 on 2025-01-04 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("FormSelector", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="EvaluationDBTable",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("fill_date", models.DateTimeField(auto_created=True, auto_now=True)),
                ("first_answer", models.CharField(max_length=255)),
                ("second_answer", models.CharField(max_length=255)),
                ("third_answer", models.CharField(max_length=255)),
                ("evaluator_name", models.CharField(max_length=255)),
                ("criteria_resp_1", models.IntegerField(default=0)),
                (
                    "criteria_resp_1_comment",
                    models.CharField(default="No Comment", max_length=255),
                ),
                ("criteria_resp_2", models.IntegerField(default=0)),
                (
                    "criteria_resp_2_comment",
                    models.CharField(default="No Comment", max_length=255),
                ),
                ("criteria_resp_3", models.IntegerField(default=0)),
                (
                    "criteria_resp_3_comment",
                    models.CharField(default="No Comment", max_length=255),
                ),
                ("criteria_resp_4", models.IntegerField(default=0)),
                (
                    "criteria_resp_4_comment",
                    models.CharField(default="No Comment", max_length=255),
                ),
                ("criteria_resp_5", models.IntegerField(default=0)),
                (
                    "criteria_resp_5_comment",
                    models.CharField(default="No Comment", max_length=255),
                ),
                ("criteria_resp_6", models.IntegerField(default=0)),
                (
                    "criteria_resp_6_comment",
                    models.CharField(default="No Comment", max_length=255),
                ),
                ("criteria_resp_7", models.IntegerField(default=0)),
                (
                    "criteria_resp_7_comment",
                    models.CharField(default="No Comment", max_length=255),
                ),
                ("criteria_resp_8", models.IntegerField(default=0)),
                (
                    "criteria_resp_8_comment",
                    models.CharField(default="No Comment", max_length=255),
                ),
                ("criteria_resp_9", models.IntegerField(default=0)),
                (
                    "criteria_resp_9_comment",
                    models.CharField(default="No Comment", max_length=255),
                ),
                ("criteria_resp_10", models.IntegerField(default=0)),
                (
                    "criteria_resp_10_comment",
                    models.CharField(default="No Comment", max_length=255),
                ),
                ("criteria_resp_11", models.IntegerField(default=0)),
                (
                    "criteria_resp_11_comment",
                    models.CharField(default="No Comment", max_length=255),
                ),
                ("criteria_resp_12", models.IntegerField(default=0)),
                (
                    "criteria_resp_12_comment",
                    models.CharField(default="No Comment", max_length=255),
                ),
                ("mail_sended", models.BooleanField(default=False)),
                (
                    "speech_evaluated",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="FormSelector.speechtoeval",
                    ),
                ),
            ],
        ),
    ]
