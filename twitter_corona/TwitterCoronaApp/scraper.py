import snscrape.modules.twitter as sntwitter


def scraper(query, since, until):
    tweets = []
    for i, tweet in enumerate(
            sntwitter.TwitterSearchScraper(query + ' since:' + since + ' until:' + until).get_items()):
        if i > 100:
            break
        tweets.append({'date': tweet.date,
                       'user': tweet.username,
                       'tweet': tweet.content})
    return tweets
