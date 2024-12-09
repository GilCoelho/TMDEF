from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect, requires_csrf_token
from django.shortcuts import render
from django.template import loader
from django.urls import reverse

from Forms.Form_Selector.models import SpeechToEval

from Forms.Evaluation_Forms.models import EvaluationDBTable
from Forms.Evaluation_Forms.forms import FeedBackForm


@csrf_protect
@requires_csrf_token
def evaluation_form(request):
    # if this is a POST request we need to process the form data
    if request.method == "GET":
        form_name = request.GET.get("form", "generic")
        speech_id = request.GET.get("speech", 0)

        # Get Speech data from db by the speech_id
        speech_to_eval = SpeechToEval.objects.get(id=speech_id)

        template = loader.get_template(f"evaluation/{form_name}_form.html")
        context = {
            "speaker": speech_to_eval.speaker,
            "speech_name": speech_to_eval.speech_name,
            "speech_id": speech_id,
        }

        return HttpResponse(template.render(context, request))


@csrf_protect
@requires_csrf_token
def feedback(request):
    form = None

    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = FeedBackForm(request.POST)

        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...

            # Get "pointer" to ForeignKey
            speech_to_eval = SpeechToEval.objects.get(id=form.cleaned_data["speech_id"])

            EvaluationDBTable(
                speech_evaluated=speech_to_eval,

                first_answer=form.cleaned_data["first_answer"],
                second_answer=form.cleaned_data["second_answer"],
                third_answer=form.cleaned_data["third_answer"],

                criteria_resp_1 = form.cleaned_data["criteria_resp_1"],
                criteria_resp_1_comment = form.cleaned_data["criteria_resp_1_comment"],

                criteria_resp_2 = form.cleaned_data["criteria_resp_2"],
                criteria_resp_2_comment = form.cleaned_data["criteria_resp_2_comment"],

                criteria_resp_3 = form.cleaned_data["criteria_resp_3"],
                criteria_resp_3_comment = form.cleaned_data["criteria_resp_3_comment"],

                criteria_resp_4 = form.cleaned_data["criteria_resp_4"],
                criteria_resp_4_comment = form.cleaned_data["criteria_resp_4_comment"],

                criteria_resp_5 = form.cleaned_data["criteria_resp_5"],
                criteria_resp_5_comment = form.cleaned_data["criteria_resp_5_comment"],

                criteria_resp_6 = form.cleaned_data["criteria_resp_6"],
                criteria_resp_6_comment = form.cleaned_data["criteria_resp_6_comment"],

                criteria_resp_7 = form.cleaned_data["criteria_resp_7"],
                criteria_resp_7_comment = form.cleaned_data["criteria_resp_7_comment"],

                criteria_resp_8 = form.cleaned_data["criteria_resp_8"],
                criteria_resp_8_comment = form.cleaned_data["criteria_resp_8_comment"],

                criteria_resp_9 = form.cleaned_data["criteria_resp_9"],
                criteria_resp_9_comment = form.cleaned_data["criteria_resp_9_comment"],

                criteria_resp_10 = form.cleaned_data["criteria_resp_10"],
                criteria_resp_10_comment = form.cleaned_data["criteria_resp_10_comment"],

                criteria_resp_11 = form.cleaned_data["criteria_resp_11"],
                criteria_resp_11_comment = form.cleaned_data["criteria_resp_11_comment"],

                criteria_resp_12 = form.cleaned_data["criteria_resp_12"],
                criteria_resp_12_comment = form.cleaned_data["criteria_resp_12_comment"],
            ).save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('evaluation:thanksForFeedBack'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FeedBackForm()

    return render(request, request.META.get('HTTP_REFERER'), {"form_questions": form})


@csrf_protect
@requires_csrf_token
def thanks_for_feedback(request):
    template = loader.get_template("thanks_for_feedback.html")
    context = {}

    return HttpResponse(template.render(context, request))
