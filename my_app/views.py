from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, template_name='base.html')


def new_search(request):
    search = request.POST.get('search')  # as we have named the placeholder search in newsearch.html
    print(search)
    stuff_for_frontend = {'search': search}
    return render(request, 'my_app/new_search.html', stuff_for_frontend)
