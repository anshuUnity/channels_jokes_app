from django.shortcuts import render
import requests

# Create your views here.


def index(request):
    raw_data = requests.get('http://api.icndb.com/jokes/random/').json()
    joke = raw_data['value']['joke']
    return render(request, 'index.html', context={'text': joke})
