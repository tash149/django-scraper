from django.shortcuts import render
from bs4 import BeautifulSoup
from requests.compat import quote_plus
import requests
from . import models

# Create your views here.

BASE_CRAIGLIST_URL = 'https://jaipur.craigslist.org/search/?query={}'#'https://jaipur.craigslist.org/search/jjj?query={}'
BASE_IMAGE_URL = 'https://images.craigslist.org/{}_300x300.jpg'

def home(request):
    return render(request, template_name='base.html')


def new_search(request):
    search = request.POST.get('search')  # as we have named the placeholder search in newsearch.html
    models.Search.objects.create(search = search)
    print(quote_plus(search))
    final_url = BASE_CRAIGLIST_URL.format(quote_plus(search))
    print(final_url)
    response = requests.get(final_url)
    data = response.text
    soup = BeautifulSoup(data, features='html.parser')

    # post_titles = soup.find_all('a', {'class': 'result-title'})
    post_listings = soup.find_all('li', {'class': 'result-row'})
    print(post_listings)

    # post_title = post_listings[0].find('a', {'class': 'result-title'}).text
    # post_url = post_listings[0].find('a').get('href')
    # post_price = post_listings[0].find('a', {'class': 'result-price'}).text

    # print(post_title)
    # print(post_url)
    # print(post_price)

    final_postings = []
    for post in post_listings:
        post_title = post.find(class_='result-title').text
        post_url = post.find('a').get('href')

        if post.find(class_='result-price'):
            post_price = post.find(class_='result-price').text
        else:
            post_price = 'N/A'

        if post.find(class_='result-image').get('data-ids'):
            post_image_id = post.find(class_= 'result-image').get('data-ids').split(',')[0].split(':')[1]
            print('>>>>>')
            post_image_url = BASE_IMAGE_URL.format(post_image_id)
            print(post_image_url)
        else:
            post_image_url = 'https://craigslist.org/images/peace.jpg'

        print(post_title)
        print(post_url)
        print(post_price)

        final_postings.append((post_title, post_url, post_price, post_image_url))

        # post_title = post.find('a', {'class': 'result-title'}).text
        # post_url = post.find('a').get('href')
        # post_price = post.find('a', {'class': 'result-price'}).text

        # final_postings.append((post_title, post_url, post_price))




    # yaha pe baaki sab kuch

    stuff_for_frontend = {
        'search': search,
        'final_postings': final_postings
    }

    return render(request, 'my_app/new_search.html', stuff_for_frontend)
    # print(post_titles[0].get('href')) # post_titles[0].text
