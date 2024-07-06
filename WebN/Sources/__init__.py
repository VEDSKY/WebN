# base imports
import json
import random
# get app config
from WebN.Config import get_env_key as WebN
# get Google News api client
from newsapi import NewsApiClient

"""

"""

"""
GOOGLE NEWS API
"""
google_news = NewsApiClient(WebN("GOOGLE_NEWS_API_KEY"))


def google_get_top_headlines(sources=None):
    news_json = json.dumps(google_news.get_top_headlines(sources=sources))
    news = json.loads(news_json)
    if news['status'] == 'ok':
        return news['articles']
    else:
        return None


def google_get_random_source():
    source = random.choice(google_news.get_sources())
