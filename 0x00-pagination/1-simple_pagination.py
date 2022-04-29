#!/usr/bin/env python3
"""
Write a function named index_range
that takes two integer arguments
page and page_size.

The function should return a tuple
of size two containing a start index
and an end index corresponding to the
range of indexes to return in a list
for those particular pagination parameters.

Page numbers are 1-indexed, i.e. the
first page is page 1.
"""
import csv
import math
from typing import List, Tuple


def index_range(page, page_size) -> Tuple[int, int]:
    """0. Simple helper function"""
    return ((page - 1) * page_size, page * page_size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Implement a method named get_page that takes two integer
            arguments page with default value 1 and page_size with
            default value 10.

            You have to use this CSV file (same as the one presented
            at the top of the project)
            Use assert to verify that both arguments are integers
            greater than 0.
            Use index_range to find the correct indexes to paginate
            the dataset correctly and return the appropriate page of
            the dataset (i.e. the correct list of rows).
            If the input arguments are out of range for the dataset,
            an empty list should be returned."""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page > 0

        self.dataset()

        if self.__dataset is None:
            return []

        idxRange = index_range(page, page_size)
        data = self.__dataset[idxRange[0]:idxRange[1]]
        return data
