#!/usr/bin/python3
"""
A Function that queries the Reddit API and returns the number of
subscribers(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given,
the function should return 0.
NOTE: Invalid subreddits may return a redirect to search results.
Ensure that you are not following redirects.
"""

import json
import requests


def number_of_subscribers(subreddit):
    headers = {'User-Agent': 'Duff'}
    url = 'https://www.reddit.com/r/' + subreddit + '/about.json'
    request = requests.get(url, headers=headers, allow_redirects=False)
    if request.status_code == 200:
        data = json.loads(request.text)
        return data['data']['subscribers']
    else:
        return 0


if __name__ == "__main__":

    print("{:d}".format(number_of_subscribers('programming')))
