#!/usr/bin/python3
"""
A recursive function that queries the Reddit API and returns
a list containing the titles of all hot articles for a given subreddit.
If no results are found for the given subreddit,
the function should return None.
If not a valid subreddit, return None.
Hint: The Reddit API uses pagination for separating pages of responses.
Hint: No authentication is necessary for most features of the Reddit API.
If you’re getting errors related to Too Many Requests,
ensure you’re setting a custom User-Agent.
This /can/ be done with a loop but the point is to use a recursive function. :)
python3 2-main.py programming
python3 2-main.py this_is_a_fake_subreddit
"""

import json
import requests


def recurse(subreddit, hot_list=[], after=None):
    headers = {'User-Agent': 'Duff'}
    url = 'https://www.reddit.com/r/' + subreddit + '/hot.json?limit=100'

    if after is not None:
        url += '&after=' + after

    request = requests.get(url, headers=headers, allow_redirects=False)

    if request.status_code == 200:
        data = json.loads(request.text)
        posts = data['data']['children']

        for post in posts:
            hot_list.append(post['data']['title'])

        if data['data']['after'] is None:
            return None

        recurse(subreddit, hot_list, data['data']['after'])
    else:
        return None

    return hot_list


if __name__ == '__main__':
    result = recurse('programming')
    if result is not None:
        print(len(result))
    else:
        print("None")
