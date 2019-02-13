from django import forms
# from django.utils.translation import gettext_lazy as _


class ContactForm(forms.Form):
    name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)
    subject = forms.CharField(max_length=100, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
    checkbox = forms.BooleanField(required=True, widget=forms.CheckboxInput)

    name.widget.attrs.update({'class': 'form-control', 'placeholder': 'Your name | Company name *'})
    email.widget.attrs.update({'class': 'form-control', 'placeholder': 'Your email *'})
    subject.widget.attrs.update({'class': 'form-control', 'placeholder': 'Subject of your message *'})
    message.widget.attrs.update({'class': 'form-control', 'placeholder': 'Your message *'})
    checkbox.widget.attrs.update({'class': 'form-check-input'})


