from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect, requires_csrf_token
from django.shortcuts import render
from django.template import loader

from django.conf import settings

from Forms.Form_Selector.models import SpeechToEval, FeedBackFormsList
from Forms.Form_Selector.forms import AddSpeechForm


# Create your views here.
@csrf_protect
@requires_csrf_token
def form_selector(request, form_data=None):
    speech_list = SpeechToEval.objects.all().values()
    fd_forms_list = FeedBackFormsList.objects.all().values()

    template = loader.get_template("form.html")
    context = {
        "speech_list": speech_list,
        "speech_feed_back_form": fd_forms_list,
        "form_data": form_data,
    }

    return HttpResponse(template.render(context, request))

@csrf_protect
@requires_csrf_token
def add_speech(request):
    form = None

    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = AddSpeechForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            SpeechToEval(
                speaker=form.cleaned_data["speaker"],
                speaker_email=form.cleaned_data["speaker_email"],
                speech_name=form.cleaned_data["speech_name"],
                pathway_challenge=form.cleaned_data["pathway_challenge"],
                feedback_form=form.cleaned_data["feedback_form"],
            ).save()

            # redirect to a new URL:
            return render(request, "thanks.html")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AddSpeechForm()

    # Return back to Selector form with form data
    return form_selector(request, form)
