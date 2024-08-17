#!/usr/bin/python3
'''

This module queries the Reddit API and gets the number of subs to a subreddit


'''
import requests


def number_of_subscribers(subreddit):
    """
    Gets the number of subscribers in a subreddit
    Returns 0 if the request is invalid
    Also returns 0 if the subreddit param is not a string
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/127.0.0.0 Safari/537.36"}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    response = response.json()
    try:
        return response.get("data").get("subscribers")
    except Exception:
        return 0
