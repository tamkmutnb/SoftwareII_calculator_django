from django import forms

class CalculationForm(forms.Form):
    user_x = forms.CharField(label='x', max_length=100)
    user_y = forms.CharField(label='y', max_length=100)
    user_operator = forms.CharField(label='operator', max_length=100)


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)