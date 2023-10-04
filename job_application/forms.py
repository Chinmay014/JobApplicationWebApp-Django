from django import forms

class ApplicationForm(forms.Form):
    first_name = forms.CharField(max_length=80)
    print(first_name)
    last_name = forms.CharField(max_length=80)
    email = forms.EmailField()
    date = forms.DateField()
    occupation = forms.CharField(max_length=80)
