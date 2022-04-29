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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Implement a get_hyper method that takes the same
        arguments (and defaults) as get_page and returns a
        dictionary containing the following key-value pairs:

            page_size: the length of the returned dataset
            page
            page: the current page number
            data: the dataset page (equivalent to return
            from previous task)
            next_page: number of the next page, None if
            no next page
            prev_page: number of the previous page, None
            if no previous page
            total_pages: the total number of pages in the
            dataset as an integer
            Make sure to reuse get_page in your implementation.

            You can use the math module if necessary."""
        data = self.get_page(page, page_size)

        dataSet = self.__dataset
        len_dataSet = len(dataSet) if dataSet else 0

        total_pages = math.ceil(len_dataSet / page_size) if dataSet else 0

        if not data:
            page_size = 0
        else:
            page_size = len(data)

        prev_page = page - 1 if page > 1 else None
        next_page = page + 1 if page < total_pages else None

        hyper = {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }

        return hyper
