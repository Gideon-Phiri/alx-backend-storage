#!/usr/bin/env python3
"""
Web caching with Redis
"""
import redis
import requests
from typing import Callable


def get_page(url: str) -> str:
    """Fetch the HTML content of a URL and cache it with an expiration"""
    r = redis.Redis()
    count_key = f"count:{url}"
    cache_key = f"cache:{url}"
    r.incr(count_key)
    cached_page = r.get(cache_key)
    if cached_page:
        return cached_page.decode('utf-8')
    response = requests.get(url)
    r.setex(cache_key, 10, response.text)
    return response.text
