#!/usr/bin/python3

"""
Prints the titles of the first 10 hot posts listed for a given subreddit.
"""

from requests import get


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts listed
    for a given subreddit.

    Parameters:
    - subreddit (str): The name of the subreddit to query.

    Returns:
    - None

    Prints the titles of the first 10 hot posts listed for the given subreddit.
    If the subreddit is not found or an error occurs during the API request, it
    prints "None".
    """

    if subreddit is None or not isinstance(subreddit, str):
        print("None")

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    params = {'limit': 10}
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)

    response = get(url, headers=user_agent, params=params)
    results = response.json()

    try:
        my_data = results.get('data').get('children')

        for i in my_data:
            print(i.get('data').get('title'))

    except Exception:
        print("None")
