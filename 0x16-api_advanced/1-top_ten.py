#!/usr/bin/python3
"""
function that queries the Reddit API and prints the
titles of the first 10 hot posts listed for a given subreddit
"""

import json
import requests


def top_ten(subreddit):
    headers = {'User-agent': 'My-User-Agent'}
    url = 'https://www.reddit.com/r/' + subreddit + '/hot.json?limit=10'
    req = requests.get(url, headers=headers, allow_redirects=False)

    if req.status_code == 200:
        postData = json.loads(req.text)['data']['children']
        for post in postData:
            print(post.get('data').get('title'))

    else:
        print('None')
