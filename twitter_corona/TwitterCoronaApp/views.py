from django.shortcuts import render

from TwitterCoronaApp import scraper


def home(request):
    if request.POST:
        form_data = request.POST.dict()
        twitter_scraper = scraper.scraper(form_data.get('tweet'), form_data.get('since'),
                                          form_data.get('until'))
        context = {'tweets': twitter_scraper}

        return render(request, '../templates/TwitterCoronaApp/home.html', context)
    else:
        return render(request, '../templates/TwitterCoronaApp/home.html')


def about(request):
    return render(request, '../templates/TwitterCoronaApp/about.html')
