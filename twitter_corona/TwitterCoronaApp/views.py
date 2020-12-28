from django.shortcuts import render
from django.http import HttpResponse

tweets = [
    {
        'date': '12.2.2020',
        'user': 'dacxo',
        'tweet': 'karona je prevara'
    },
    {
        'date': '25.7.2020',
        'user': 'fugo88',
        'tweet': 'sezona gori'
    },
    {'date': '19.11.2020',
     'user': 'antonio_markulinovic',
     'tweet': 'crkla mi krava od karone'
     }
]


def home(request):
    context = {'tweets': tweets}
    return render(request, '../templates/TwitterCoronaApp/home.html', context)


def about(request):
    return render(request, '../templates/TwitterCoronaApp/about.html')
