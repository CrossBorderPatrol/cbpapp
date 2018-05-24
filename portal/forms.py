from django import forms

IDENTIFIER_CHOICES = (
    ('passport', 'Passport'),
)

class SubjectOfInterestRequestForm(forms.Form):
    code_name = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Reciprocity',
        }),
    )
    name = forms.CharField(
        required=True,
        initial="JOHNIE BAUMKIRCHNER",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'JOHNIE BAUMKIRCHNER',
        }),
    )
    address = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '10 Downing Street',
        }),
    )
    #subject_identifier_type = forms.MultipleChoiceField(
    #    widget=forms.RadioSelect,
    #    choices=IDENTIFIER_CHOICES,
    #)
    subject_identifier = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'XXX-XX-XXXX',
        }),
    )
    account = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            # 'placeholder': 'Write your name here',
        }),
    )
