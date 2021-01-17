import snscrape.modules.twitter as sntwitter


def scraper(query, since, until):
    tweets = []
    # since = datetime.strptime(since, '%Y-%m-%d')
    # until = datetime.strptime(until, '%Y-%m-%d')
    for i, tweet in enumerate(
            sntwitter.TwitterSearchScraper(query + ' since:' + since + ' until:' + until).get_items()):
        if i > 100:
            break
        # sntwitter.TwitterSearchScraper(query + ' since:' + since + ' until:' + until).get_items()):
        tweets.append({'date': tweet.date,
                       'user': tweet.user.username,
                       'tweet': tweet.content})
    return tweets
