from django.shortcuts import render
from techblog.models import TechblogPage
from wagtail.search.models import Query
from wagtail.core.models import Page


def index(request):
    blogpages = TechblogPage.objects.live().order_by('-date')

    return render(request, 'techblog/index.html', {
        'blogpages': blogpages,
    })


def searchIndex(request):
    search_query = request.GET.get('query', None)
    if search_query:
        blogpages = TechblogPage.objects.live().search(search_query)
        Query.get(search_query).add_hit()
        empty_search = False
    else:
        blogpages = Page.objects.none()
        search_query = ''
        empty_search = True

    return render(request, 'techblog/search.html', {
        'blogpages': blogpages,
        'search_query': search_query,
        'empty_search': empty_search,
    })


def categoryIndex(request):
    category = request.GET.get('category')
    blogpages = TechblogPage.objects.live().filter(categories__name=category).order_by('-date')

    return render(request, 'techblog/category_index.html', {
        'blogpages': blogpages,
    })


def tagIndex(request):
    tag = request.GET.get('tag')
    blogpages = TechblogPage.objects.live().filter(tags__name=tag).order_by('-date')

    return render(request, 'techblog/tag_index.html', {
        'blogpages': blogpages,
    })

