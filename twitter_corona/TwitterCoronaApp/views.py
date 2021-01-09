from django.shortcuts import render

from TwitterCoronaApp import scraper

from TwitterCoronaApp import sentiment


def home(request):
    if request.POST:
        form_data = request.POST.dict()
        twitter_scraper = scraper.scraper(form_data.get('tweet'), form_data.get('since'),
                                          form_data.get('until'))
        context = {'tweets': twitter_scraper}
        tweets_sentiment = []
        for tw in twitter_scraper:
            tweets_sentiment.append(tw.get('tweet'))

        sentiment.getSentiment(tweets_sentiment, form_data.get('tweet'))

        return render(request, '../templates/TwitterCoronaApp/home.html', context)
    else:
        return render(request, '../templates/TwitterCoronaApp/home.html')


def about(request):
    return render(request, '../templates/TwitterCoronaApp/about.html')
