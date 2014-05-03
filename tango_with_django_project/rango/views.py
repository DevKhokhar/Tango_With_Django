from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from models import Category, Page

def index(request):
    context = RequestContext(request)

    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}
    for category in category_list:
        category.url = encode_category_url(category.name)

    page_list = Page.objects.order_by('-views')[:5]
    context_dict['pages'] = page_list

    return render_to_response('rango/index.html', context_dict, context)

def about(request):
    return HttpResponse("Rango Says: Here is the about page. <a href='/rango/'>Index</a>")

def category(request, category_name_url):
    context = RequestContext(request)

    category_name = decode_category_name_url(category_name_url)

    context_dict = {'category_name': category_name}

    try:
        category = Category.objects.get(name=category_name)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        pass

    return render_to_response('rango/category.html', context_dict, context)

def decode_category_name_url(category_name_url):
    return category_name_url.replace('_', ' ')

def encode_category_url(category_name):
    return category_name.replace(' ', '_')