from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect, requires_csrf_token
from django.shortcuts import render
from django.template import loader

from django.conf import settings

from Forms.IceBreaker_Evaluation_8101.models import EvaluationForm
from Forms.IceBreaker_Evaluation_8101.forms import FeedBackForm


# Create your views here.
@csrf_protect
@requires_csrf_token
def evaluation_form(request):
    template = loader.get_template("icebreaker_form.html")
    context = {}

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
            EvaluationForm(
                first_answer=form.cleaned_data["first_answer"],
                second_answer=form.cleaned_data["second_answer"],
                third_answer=form.cleaned_data["third_answer"],
            ).save()

            # redirect to a new URL:
            return HttpResponseRedirect("/thanks/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FeedBackForm()

    return render(request, "thanks.html", {"form": form})
