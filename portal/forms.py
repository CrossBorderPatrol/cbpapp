from django import forms

IDENTIFIER_CHOICES = (
    ('passport', 'Passport'),
)

class SubjectOfInterestRequestForm(forms.Form):
    code_name = forms.CharField()
    name = forms.CharField(required=True, initial="JOHNIE BAUMKIRCHNER")
    address = forms.CharField(widget=forms.Textarea)
    #subject_identifier_type = forms.MultipleChoiceField(
    #    widget=forms.RadioSelect,
    #    choices=IDENTIFIER_CHOICES,
    #)
    subject_identifier = forms.CharField()
    account = forms.CharField()
