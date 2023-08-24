#!/usr/bin/python3
""" Python caching systems """
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """ LRU caching system"""

    def __init__(self):
        """ Initializing class instance. """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ adding item to the cache"""
        if key and item:
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discarded = self.cache_data.popitem(last=False)
                print('DISCARD: {}'.format(discarded[0]))

    def get(self, key):
        """ retrieving item with key """
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
