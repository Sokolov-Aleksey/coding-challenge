__author__ = 'alex'

import sys
from tweets_cleaned import TweetCleaner
from average_degree import HashGraph

if __name__ == "__main__":
    sys.argv = ['','../tweet_input/tweets.txt', '../tweet_output/ft1.txt', '../tweet_output/ft2.txt']
    input_path = sys.argv[1] # tweets.txt
    output_clean = open(sys.argv[2], 'w') # ft1.txt
    output_average = open(sys.argv[3], 'w') #ft2.txt

    cleaner = TweetCleaner()
    graph = HashGraph()

    with open(input_path, "r+") as tweets:
        for tweet in tweets:
            try:
                # the first feature , clean and write to ft1.txt

                # extract timestamp and text from json and clean each tweet from unicode
                cleaned = cleaner.clean(tweet)
                output_clean.write(cleaned+'\n')

                # the second feature, find avg get_avg_degree and write to ft2.txt

                tags, timestamp = cleaner.extract_tags_time(cleaned)
                graph.process_tweet(tags, timestamp)
                output_average.write("%.2f" % graph.get_avg_degree()+'\n')
            except KeyError: # Testing suite shouldn't have key errors, but the sample tweets.txt contains the "limit objects"
                pass
    output_clean.write('\n%s tweets contained unicode.' % cleaner.unicode_tweets)


