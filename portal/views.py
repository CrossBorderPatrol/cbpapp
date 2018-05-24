import json
import logging

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import FormView

from portal.forms import SubjectOfInterestRequestForm
from core.views import HashedNameServiceClient, N1AnalyticsClient

logger = logging.getLogger(__name__)

# Create your views here.
def index(request):
    return HttpResponseRedirect(reverse('portal:subject-of-interest-request-add'))
    # return render(request, 'portal/home.html')
    # return HttpResponse("Hello, world. You're at the portal index.")


def subject_of_interest_request(request):
    if request.method == 'POST':
        form = SubjectOfInterestRequestForm(request.POST)

        if form.is_valid():
            #return JsonResponse(form.cleaned_data)

            name = form.cleaned_data['name']
            hasher = HashedNameServiceClient()

            hashed = hasher.name_to_hash(name)

            n1 = N1AnalyticsClient()
            response = n1.get_bank_runs(hashed)

            return render(request, 'portal/home.html', {'form': form, 'response': response})

            pass  # does nothing, just trigger the validation
        else:
            raise Exception(form.errors)
    else:
        form = SubjectOfInterestRequestForm()
    return render(request, 'portal/home.html', {'form': form})

def subject_of_interest_request_detail(request):
    token = request.GET["token"]

    hasher = HashedNameServiceClient()
    response = hasher.hash_to_info(token)

    logger.error("details: " + json.dumps(response))
    logger.error(type(response))

    r = json.loads(response)
    logger.error(type(r))

    return render(request, 'portal/subject_of_interest_request_detail.html', {'token': token, 'response': r})

class SubjectOfInterestRequestView(FormView):
    template_name = 'subject_of_interest_request.html'
    form_class = SubjectOfInterestRequestForm
    success_url = '/thanks/'

    # def form_valid(self, form):
    #     # This method is called when valid form data has been POSTed.
    #     # It should return an HttpResponse.
    #     form.send_email()
    #     return super().form_valid(form)
