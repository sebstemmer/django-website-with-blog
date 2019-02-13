from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ContactForm
from django.urls import reverse
from django.core.mail import send_mail, BadHeaderError


def index(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            complete_message = 'Name: ' + name + '\n\n' + message

            try:
                send_mail(subject, complete_message, email, ['contact.stemmer@gmail.com'], fail_silently=True)
            except BadHeaderError:
                return HttpResponseRedirect(reverse('contact_error'))
            return HttpResponseRedirect(reverse('contact_success'))
        else:
            return HttpResponseRedirect(reverse('contact_error'))

    else:
        form = ContactForm()

    context = {
        'form': form,
    }

    return render(
        request,
        'mainpage/index.html',
        context,
    )


def legalnotice_de(request):
    return render(
        request,
        'mainpage/legalnotice_de.html',
    )


def legalnotice_en(request):
    return render(
        request,
        'mainpage/legalnotice_en.html',
    )


def privacy_de(request):
    return render(
        request,
        'mainpage/privacy_de.html',
    )


def privacy_en(request):
    return render(
        request,
        'mainpage/privacy_en.html',
    )


def contact_success(request):
    return render(
        request,
        'mainpage/contact_success.html',
    )


def contact_error(request):
    return render(
        request,
        'mainpage/contact_error.html',
    )
