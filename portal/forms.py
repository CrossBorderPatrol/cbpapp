from django import forms

IDENTIFIER_CHOICES = (
    ('passport', 'Passport'),
)

class SubjectOfInterestRequestForm(forms.Form):
    code_name = forms.CharField(required=False)
    name = forms.CharField(required=True, initial="JOHNIE BAUMKIRCHNER")
    address = forms.CharField(required=False, widget=forms.Textarea)
    #subject_identifier_type = forms.MultipleChoiceField(
    #    widget=forms.RadioSelect,
    #    choices=IDENTIFIER_CHOICES,
    #)
    subject_identifier = forms.CharField(required=False)
    account = forms.CharField(required=False)
