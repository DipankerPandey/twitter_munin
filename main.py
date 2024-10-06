#!/usr/bin/env python

import sys
import argparse
from collections import OrderedDict
from twitter import Twitter, OAuth
from pprint import pprint

def get_twitter_client(config_file):
    """Read Twitter API credentials from a config file instead of hardcoding and return a Twitter client."""
    config = {}
    with open(config_file, 'r') as f:
        for line in f:
            key, value = line.strip().split('=')
            config[key.strip()] = value.strip()

    return Twitter(auth=OAuth(config['OAUTH_TOKEN'], config['OAUTH_SECRET'],
                              config['CONSUMER_KEY'], config['CONSUMER_SECRET']))

def get_user_stats(twitter_client, screen_name, tweet_count=200):
    """Fetch and analyze tweets for the given user."""
    tweets = twitter_client.statuses.user_timeline(count=tweet_count, screen_name=screen_name)
    
    count = 0
    favs = 0
    retweets = 0

    for tweet in tweets:
        if tweet['user']['screen_name'] == screen_name and not tweet['text'].startswith("RT"):
            count += 1
            favs += tweet['favorite_count']
            retweets += tweet['retweet_count']

    return {
        "tweets_analyzed": count,
        "avg_favorites": favs / count if count > 0 else 0,
        "avg_retweets": retweets / count if count > 0 else 0
    }

def main():
    parser = argparse.ArgumentParser(description="Analyze Twitter user stats.")
    parser.add_argument("config_file", help="Path to the config file containing Twitter API credentials")
    parser.add_argument("screen_name", help="Twitter screen name to analyze")
    parser.add_argument("--tweet-count", type=int, default=200, help="Number of tweets to analyze (default: 200)")
    parser.add_argument("--output-format", choices=["human", "munin"], default="human", help="Output format (default: human)")
    args = parser.parse_args()

    try:
        twitter_client = get_twitter_client(args.config_file)
        stats = get_user_stats(twitter_client, args.screen_name, args.tweet_count)

        if args.output_format == "human":
            print(f"Stats for @{args.screen_name}:")
            print(f"Tweets analyzed: {stats['tweets_analyzed']}")
            print(f"Average favorites per tweet: {stats['avg_favorites']:.2f}")
            print(f"Average retweets per tweet: {stats['avg_retweets']:.2f}")
        elif args.output_format == "munin":
            print(f"favorite.value {stats['avg_favorites']:.2f}")
            print(f"retweet.value {stats['avg_retweets']:.2f}")

    except Exception as e:
        print(f"An error occurred: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()