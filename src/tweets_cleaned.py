# example of program that calculates the number of tweets cleaned
import re
import time

# we'll get a performance boost if ujson is available
try:
    import ujson as json
except ImportError:
    import json

class TweetCleaner(object):
    def __init__(self):
        self.unicode_tweets = 0

    def clean(self, tweet):
        tweet = json.loads(tweet)
        timestamp = tweet["created_at"]
        text = tweet["text"].replace("\n", " ").replace("\t", " ")
        cleaned = text.encode('utf-8').decode('unicode_escape').encode('ascii', 'ignore')
        if len(cleaned) != len(text):
            self.unicode_tweets += 1
        return '%s (timestamp: %s)' % (cleaned, timestamp)

    def extract_tags_time(self, tweet):
        # Used for extracting all hastags from cleaned tweets.
        HASHTAG_RE = re.compile(r"#(\w+)")
        # Used to extract timestamp from cleaned tweets.
        TS_RE = re.compile(r"\(timestamp: (.+)\)")
        hashtags = HASHTAG_RE.findall(tweet)
        dt = time.strptime(TS_RE.findall(tweet)[0], '%a %b %d %H:%M:%S +0000 %Y')
        # lowercase tags, get rid of possible duplicates, sort for later use
        hashtags = sorted(set(map(unicode.lower,hashtags)))
        return hashtags, time.mktime(dt)