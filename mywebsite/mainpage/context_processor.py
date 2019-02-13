from django.conf import settings


def ga(request):
    context_pre = {'DEBUG': settings.DEBUG}
    if settings.DEBUG is False:
        context_pre['GA_TRACKING_ID'] = settings.GA_TRACKING_ID

    return context_pre


def private_data(request):
    context_pre = {
        'PRIVATE_DATA_STREET': settings.PRIVATE_DATA_STREET,
        'PRIVATE_DATA_PHONE': settings.PRIVATE_DATA_PHONE,
    }
    return context_pre
