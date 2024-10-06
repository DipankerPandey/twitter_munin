# Twitter Stats Analyzer

This Python script analyzes the latest tweets of a specified Twitter user and generates statistics that can be used to create a Munin graph. It calculates the average number of favorites and retweets per tweet.

## Features

- Analyzes up to 200 recent tweets (configurable) of a specified Twitter user
- Calculates average favorites and retweets per tweet
- Outputs results in human-readable or Munin-compatible format
- Uses external configuration file for Twitter API credentials

## Prerequisites

- Python 3.6 or higher
- `twitter` library (install with `pip install twitter`)
- Twitter Developer account and API credentials

## Setup

1. Clone this repository or download the script.

2. Install the required library:
   ```
   pip install twitter
   ```

3. Create a Twitter Developer account and set up an application to get your API credentials.

4. Create a configuration file named `twitter_config.ini` in the same directory as the script with your Twitter API credentials:
   ```
   OAUTH_TOKEN=your_oauth_token
   OAUTH_SECRET=your_oauth_secret
   CONSUMER_KEY=your_consumer_key
   CONSUMER_SECRET=your_consumer_secret
   ```

## Usage

Run the script from the command line with the following syntax:

```
python twitter_stats.py <config_file> <screen_name> [--tweet-count <count>] [--output-format <format>]
```

- `<config_file>`: Path to your Twitter API credentials configuration file
- `<screen_name>`: Twitter screen name to analyze (without '@')
- `--tweet-count`: (Optional) Number of tweets to analyze (default: 200)
- `--output-format`: (Optional) Output format, either 'human' or 'munin' (default: 'human')

### Examples

1. Analyze the last 200 tweets of user 'example_user' with human-readable output:
   ```
   python twitter_stats.py twitter_config.ini example_user
   ```

2. Analyze the last 500 tweets of user 'example_user' with Munin-compatible output:
   ```
   python twitter_stats.py twitter_config.ini example_user --tweet-count 500 --output-format munin
   ```

## How It Works

1. The script reads Twitter API credentials from the specified configuration file.
2. It creates a Twitter client using these credentials.
3. The script fetches the specified number of recent tweets for the given user.
4. It analyzes these tweets, counting only original tweets (not retweets) by the specified user.
5. The script calculates the average number of favorites and retweets per tweet.
6. Finally, it outputs the results in either human-readable or Munin-compatible format.

## Output Formats

1. Human-readable format:
   ```
   Stats for @example_user:
   Tweets analyzed: 200
   Average favorites per tweet: 10.50
   Average retweets per tweet: 2.75
   ```

2. Munin-compatible format:
   ```
   favorite.value 10.50
   retweet.value 2.75
   ```

## Notes

- The script respects Twitter's API rate limits.
- Ensure your Twitter Developer account has the necessary permissions to read user timelines.
- Keep your API credentials confidential and do not share them publicly.
