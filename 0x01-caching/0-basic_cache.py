#!/usr/bin/python3
"""caching in dictionary"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Adding more items in the dictionary"""

    def put(self, key, item):
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):

        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
