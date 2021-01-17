import os
from flask import Flask
from django.shortcuts import render

from TwitterCoronaApp import scraper

from TwitterCoronaApp import sentiment

app = Flask(__name__)


@app.route("/")
def hello(request):
    if request.POST:
        form_data = request.POST.dict()
        twitter_scraper = scraper.scraper(form_data.get('tweet'), form_data.get('since'),
                                          form_data.get('until'))
        tweets_sentiment = []
        for tw in twitter_scraper:
            tweets_sentiment.append(tw.get('tweet'))

        sentiment_image = sentiment.getSentiment(tweets_sentiment, form_data.get('tweet'))

        return render(request, '../templates/TwitterCoronaApp/home.html', {'tweets': twitter_scraper,
                                                                           'sentiment_image': sentiment_image})
    else:
        return render(request, '../templates/TwitterCoronaApp/home.html')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
