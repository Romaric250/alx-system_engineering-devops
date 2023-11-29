#!/usr/bin/python3
"""
this api gives the number of subscribers for a given subreddit
"""

from requests import get


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers (total subscribers,
    not active users) for a given subreddit.

    Parameters:
    - subreddit (str): The name of the subreddit to query.

    Returns:
    - int: The number of subscribers for the given subreddit. Returns 0 if the
      subreddit is not found or an error occurs during the API request.
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(url, headers=user_agent)
    results = response.json()

    try:
        return results.get('data').get('subscribers')

    except Exception:
        return 0
