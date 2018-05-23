from django.urls import path

from . import views
from portal.views import SubjectOfInterestRequestView

urlpatterns = [
    path('', views.index, name='index'),
    path('subject-of-interest-request/', views.subject_of_interest_request, name='subject-of-interest-request-add'),
    path('subject-of-interest-request/detail', views.subject_of_interest_request_detail, name='subject-of-interest-request-add'),
    # path('subject-of-interest-request/add', SubjectOfInterestRequestView.as_view(), name='subject-of-interest-request-add'),
]
