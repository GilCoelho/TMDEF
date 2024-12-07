from django import forms


class FeedBackForm(forms.Form):
    first_answer = forms.CharField(label="first_answer", max_length=255)
    second_answer = forms.CharField(label="second_answer", max_length=255)
    third_answer = forms.CharField(label="third_answer", max_length=255)
