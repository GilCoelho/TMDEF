from django import forms


class AddSpeechForm(forms.Form):
    speaker = forms.CharField(label="speaker", max_length=255)
    speaker_email = forms.CharField(label="speaker_email", max_length=255)
    speech_name = forms.CharField(label="speech_name", max_length=255)
    pathway_challenge = forms.CharField(label="pathway_challenge", max_length=255)
    feedback_form = forms.CharField(
        label="pathway_challenge", max_length=255
    )  # forms.Select()
