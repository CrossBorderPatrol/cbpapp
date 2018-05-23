from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import FormView

from portal.forms import SubjectOfInterestRequestForm

# Create your views here.
def index(request):
    return HttpResponseRedirect(reverse('portal:subject-of-interest-request-add'))
    # return render(request, 'portal/home.html')
    # return HttpResponse("Hello, world. You're at the portal index.")


def subject_of_interest_request(request):
    if request.method == 'POST':
        form = SubjectOfInterestRequestForm(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = SubjectOfInterestRequestForm()
    return render(request, 'portal/home.html', {'form': form})


class SubjectOfInterestRequestView(FormView):
    template_name = 'subject_of_interest_request.html'
    form_class = SubjectOfInterestRequestForm
    success_url = '/thanks/'

    # def form_valid(self, form):
    #     # This method is called when valid form data has been POSTed.
    #     # It should return an HttpResponse.
    #     form.send_email()
    #     return super().form_valid(form)
