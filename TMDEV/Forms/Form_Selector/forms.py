from django import forms

REQUIRED_ERROR_MESSAGE = "This Filed is required"

class AddSpeechForm(forms.Form):
    speaker = forms.CharField(label="speaker", max_length=255, required=True, error_messages={"required": REQUIRED_ERROR_MESSAGE})
    speaker_email = forms.CharField(label="speaker_email", max_length=255, required=True, error_messages={"required": REQUIRED_ERROR_MESSAGE})
    speech_name = forms.CharField(label="speech_name", max_length=255, required=True, error_messages={"required": REQUIRED_ERROR_MESSAGE})
    pathway_challenge = forms.CharField(label="pathway_challenge", max_length=255, required=True, error_messages={"required": REQUIRED_ERROR_MESSAGE})
    feedback_form = forms.CharField(
        label="pathway_challenge", max_length=255, required=True, error_messages={"required": REQUIRED_ERROR_MESSAGE}
    )  # forms.Select()
