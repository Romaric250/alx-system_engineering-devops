#!/usr/bin/python3
"""Reddit API"""

import json
import requests


def count_words(subreddit, word_list, after="", word_count=[]):
    """Count occurrences of words"""

    if after == "":
        word_count = [0] * len(word_list)

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url,
                            params={'after': after},
                            allow_redirects=False,
                            headers={'user-agent': 'bhalut'})

    if response.status_code == 200:
        data = response.json()

        for topic in data['data']['children']:
            for word in topic['data']['title'].split():
                for i in range(len(word_list)):
                    if word_list[i].lower() == word.lower():
                        word_count[i] += 1

        after = data['data']['after']
        if after is None:
            save_indices = []
            for i in range(len(word_list)):
                for j in range(i + 1, len(word_list)):
                    if word_list[i].lower() == word_list[j].lower():
                        save_indices.append(j)
                        word_count[i] += word_count[j]

            for i in range(len(word_list)):
                for j in range(i, len(word_list)):
                    if (word_count[j] > word_count[i] or
                            (word_list[i] > word_list[j] and
                             word_count[j] == word_count[i])):
                        word_count[i], word_count[j] = word_count[j], word_count[i]
                        word_list[i], word_list[j] = word_list[j], word_list[i]

            for i in range(len(word_list)):
                if word_count[i] > 0 and i not in save_indices:
                    print("{}: {}".format(word_list[i].lower(), word_count[i]))
        else:
            count_words(subreddit, word_list, after, word_count)
