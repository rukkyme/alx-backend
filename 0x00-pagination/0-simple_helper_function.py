#!/usr/bin/env python3

"""
function named index_range that takes two integer arguments
page and page_size
"""


def index_range(page: int, page_size: int):
    """Generate list index range"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
