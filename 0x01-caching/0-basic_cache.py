#!/usr/bin/env python3
"""caching in dictionary"""
from base_caching import BaseCaching

"""BasicCache inherits from BaseCaching"""
class BasicCache(BaseCaching):
    
    def put(self, key, item):
        """Adding more items in the dictionary"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """retrieves item in the dictionary"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
