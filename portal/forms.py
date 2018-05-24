from django import forms

IDENTIFIER_CHOICES = (
    ('passport', 'Passport'),
)

class SubjectOfInterestRequestForm(forms.Form):
    code_name = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={ 'class': 'form-control' }),
    )
    name = forms.CharField(
        required=True,
        initial="JOHNIE BAUMKIRCHNER",
        widget=forms.TextInput(attrs={ 'class': 'form-control' }),
    )
    address = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={ 'class': 'form-control' }),
    )
    #subject_identifier_type = forms.MultipleChoiceField(
    #    widget=forms.RadioSelect,
    #    choices=IDENTIFIER_CHOICES,
    #)
    subject_identifier = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={ 'class': 'form-control' }),
    )
    account = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={ 'class': 'form-control' }),
    )
