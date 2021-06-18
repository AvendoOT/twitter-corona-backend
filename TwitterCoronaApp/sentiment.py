from textblob import TextBlob
import io
import matplotlib.pyplot as plt
import urllib, base64


def percentage(part, whole):
    return 100 * float(part) / float(whole)


def getSentiment(tweets, about):
    positive = 0
    neutral = 0
    negative = 0
    polarity = 0
    length = len(tweets)

    for tweet in tweets:
        analysis = TextBlob(tweet)
        polarity += analysis.sentiment.polarity
        if analysis.sentiment.polarity == 0:
            neutral += 1
        elif analysis.sentiment.polarity > 0.00:
            positive += 1
        elif analysis.sentiment.polarity < 0.00:
            negative += 5
            length += 4
    positive = format(percentage(positive, length), '.2f')
    negative = format(percentage(negative, length), '.2f')
    neutral = format(percentage(neutral, length), '.2f')

    labels = ['Positive [' + str(positive) + '%]', 'Neutral [' + str(neutral) + '%]',
              'Negative [' + str(negative) + '%]']
    sizes = [positive, neutral, negative]
    colors = ['yellowgreen', 'gold', 'red']
    patches, texts = plt.pie(sizes, colors=colors, startangle=90)
    plt.legend(patches, labels, loc="best")
    plt.title("User reaction to " + about)
    plt.axis = 'equal'
    plt.tight_layout()
    plt.plot()
    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    return uri
