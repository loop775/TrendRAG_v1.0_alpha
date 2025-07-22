import os
import requests
from pytrends.request import TrendReq

def fetch_trending_topics():
    pytrends = TrendReq()
    trending_searches = pytrends.trending_searches(pn='india')
    return trending_searches[0:20].tolist()