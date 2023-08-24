#!/usr/bin/env python3
""" Python caching systems """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ using FIFO  """
    def __init__(self):
        """ Initializing class instance and calling it. """
        super().__init__()

    def put(self, key, item):
        """ Adding item in the cache """
        if key and item:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discarded_key = sorted(self.cache_data)[0]
            self.cache_data.pop(discarded_key)
            print('DISCARD: {}'.format(discarded_key))

    def get(self, key):
        """ retrieving item with key """
        return self.cache_data.get(key)
    