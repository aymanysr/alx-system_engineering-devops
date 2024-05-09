#!/usr/bin/python3
"""
a recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit.
If no results are found for the given subreddit,
the function should return None.
"""

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """
    Recursively query the Reddit API and return a list of all hot posts
    for a given subreddit.
    """
    # Define the base URL for the Reddit API
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    # Define headers for the HTTP request, including User-Agent
    headers = {"User-Agent": "Mozilla/5.0"}

    # Define params for the request, including the 'after' parameter
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }

    # Send a GET request to the subreddit's hot posts page
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    # Check if the response status code indicates a not-found error (404)
    if response.status_code == 404:
        return None

    # Parse the JSON response and extract the 'data' section
    results = response.json().get("data")

    # Extract the 'children' section from the 'data' section
    children = results.get("children")

    # Extract the 'after' parameter from the 'data' section
    after = results.get("after")

    # Extract the 'count' parameter from the 'data' section
    count = results.get("dist")

    # Append the titles of the current page of hot posts to the hot_list
    for chld in children:
        hot_list.append(chld.get("data").get("title"))

    # If the 'after' parameter is not None, recursively query the next page
    if after is not None:
        return recurse(subreddit, hot_list, after, count)

    return hot_list if hot_list else None
