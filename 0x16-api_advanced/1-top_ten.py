#!/usr/bin/python3

"""
prints titles of the first 10 hot posts
listed for a given subreddit
"""

from requests import get


def top_ten(subreddit):
    """
    function to querry the Reddit API and prints titles of the first
    10 hot posts listed for a subreddit
    """

    if subreddit is None or not isinstance(subreddit, str):
        print("None")

    user_agent = {'User-agent': 'Google Chrome Version 115.0.5790.171'}
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
