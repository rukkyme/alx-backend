#!/usr/bin/python3
""" Python caching systems """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ using LIFO"""

    def __init__(self):
        """ Initializing instance of the class. """
        super().__init__()

    def put(self, key, item):
        """ adding item to  the cache """
        if key and item:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            self.cache_data.pop(self.last_item)
            print('DISCARD:', self.last_item)
        if key:
            self.last_item = key

    def get(self, key):
        """ retrieving item with the key """
        return self.cache_data.get(key)
