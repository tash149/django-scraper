from django.shortcuts import render
from bs4 import BeautifulSoup
from requests.compat import quote_plus
import requests

# Create your views here.

BASE_CRAIGLIST_URL = 'https://jaipur.craigslist.org/search/jjj?query={}'


def home(request):
    return render(request, template_name='base.html')


def new_search(request):
    search = request.POST.get('search')  # as we have named the placeholder search in newsearch.html
    print(quote_plus(search))
    final_url = BASE_CRAIGLIST_URL.format(quote_plus(search))
    print('>>>>')
    print(final_url)
    response = requests.get(final_url)
    data = response.text

    stuff_for_frontend = {'search': search}
    return render(request, 'my_app/new_search.html', stuff_for_frontend)
