from django import forms

REQUIRED_ERROR_MESSAGE = "Please provide feed-back"
EMPTY_COMMENT = "No Comment"

class FeedBackForm(forms.Form):
    speech_id = forms.IntegerField(label="speech_id")

    first_answer = forms.CharField(label="first_answer", max_length=255, required=True, error_messages={"required": REQUIRED_ERROR_MESSAGE})
    second_answer = forms.CharField(label="second_answer", max_length=255, required=True, error_messages={"required": REQUIRED_ERROR_MESSAGE})
    third_answer = forms.CharField(label="third_answer", max_length=255, required=True, error_messages={"required": REQUIRED_ERROR_MESSAGE})

    evaluator_name = forms.CharField(label="evaluator_name", max_length=255)

    criteria_resp_1 = forms.IntegerField(required=False, label="criteria_resp_1", initial=0)
    criteria_resp_1_comment = forms.CharField(required=False, label="criteria_resp_1_comment", max_length=255, initial=EMPTY_COMMENT)

    criteria_resp_2 = forms.IntegerField(required=False, label="criteria_resp_2", initial=0)
    criteria_resp_2_comment = forms.CharField(required=False, label="criteria_resp_2_comment", max_length=255, initial=EMPTY_COMMENT)

    criteria_resp_3 = forms.IntegerField(required=False, label="criteria_resp_3", initial=0)
    criteria_resp_3_comment = forms.CharField(required=False, label="criteria_resp_3_comment", max_length=255, initial=EMPTY_COMMENT)

    criteria_resp_4 = forms.IntegerField(required=False, label="criteria_resp_4", initial=0)
    criteria_resp_4_comment = forms.CharField(required=False, label="criteria_resp_4_comment", max_length=255, initial=EMPTY_COMMENT)

    criteria_resp_5 = forms.IntegerField(required=False, label="criteria_resp_5", initial=0)
    criteria_resp_5_comment = forms.CharField(required=False, label="criteria_resp_5_comment", max_length=255, initial=EMPTY_COMMENT)

    criteria_resp_6 = forms.IntegerField(required=False, label="criteria_resp_6", initial=0)
    criteria_resp_6_comment = forms.CharField(required=False, label="criteria_resp_6_comment", max_length=255, initial=EMPTY_COMMENT)

    criteria_resp_7 = forms.IntegerField(required=False, label="criteria_resp_7", initial=0)
    criteria_resp_7_comment = forms.CharField(required=False, label="criteria_resp_7_comment", max_length=255, initial=EMPTY_COMMENT)

    criteria_resp_8 = forms.IntegerField(required=False, label="criteria_resp_8", initial=0)
    criteria_resp_8_comment = forms.CharField(required=False, label="criteria_resp_8_comment", max_length=255, initial=EMPTY_COMMENT)

    criteria_resp_9 = forms.IntegerField(required=False, label="criteria_resp_9", initial=0)
    criteria_resp_9_comment = forms.CharField(required=False, label="criteria_resp_9_comment", max_length=255, initial=EMPTY_COMMENT)

    criteria_resp_10 = forms.IntegerField(required=False, label="criteria_resp_10", initial=0)
    criteria_resp_10_comment = forms.CharField(required=False, label="criteria_resp_10_comment", max_length=255, initial=EMPTY_COMMENT)

    criteria_resp_11 = forms.IntegerField(required=False, label="criteria_resp_11", initial=0)
    criteria_resp_11_comment = forms.CharField(required=False, label="criteria_resp_11_comment", max_length=255, initial=EMPTY_COMMENT)

    criteria_resp_12 = forms.IntegerField(required=False, label="criteria_resp_12", initial=0)
    criteria_resp_12_comment = forms.CharField(required=False, label="criteria_resp_12_comment", max_length=255, initial=EMPTY_COMMENT)
