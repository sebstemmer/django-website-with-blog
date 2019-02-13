from django import template
from techblog.models import TechblogCategory
from utils import grouper

register = template.Library()


@register.inclusion_tag('techblog/categories_tags.html', takes_context=True)
def categories(context):
    allCategories = TechblogCategory.objects.all()
    numCategories = len(allCategories)
    if numCategories is not 0:
        if numCategories % 2 == 0:
            leftColCategories = allCategories[0:int(numCategories / 2)]
            rightColCategories = allCategories[int(numCategories / 2):numCategories]
        else:
            leftColCategories = allCategories[0:int(numCategories / 2 + 0.5)]
            rightColCategories = allCategories[int(numCategories / 2 + 0.5):numCategories]
    else:
        leftColCategories = None
        rightColCategories = None

    return {
        'leftColCategories': leftColCategories,
        'rightColCategories': rightColCategories,
        'request': context['request'],
    }
