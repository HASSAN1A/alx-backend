#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Implement a get_hyper_index method
        with two integer arguments:
        index with a None default value and page_size with
        default value of 10.

        The method should return a dictionary with the
        following key-value pairs:
        index: the current start index of the return page.
        That is the index of
        the first item in the current page. For example if
        requesting page 3 with
        page_size 20, and no data was removed from the dataset,
        the current index
        should be 60.
        next_index:
        the next index to query with. That should be the index of the
        first item after the last item on the current page.
        page_size: the current page size
        data: the actual page of the dataset
        Requirements/Behavior:

        Use assert to verify that index is in a valid range.
        If the user queries index 0, page_size 10, they will
        get rows indexed 0 to
        9 included.
        If they request the next index (10) with page_size 10,
        but rows 3, 6 and 7
        were deleted, the user should still receive rows indexed
        10 to 19 included.
        """
        idxDataSet = self.indexed_dataset()

        assert isinstance(index, int) and index < (len(idxDataSet) - 1)

        i, move, data = 0, index, []
        while (i < page_size and index < len(idxDataSet)):
            value = idxDataSet.get(move, None)
            if value:
                data.append(value)
                i += 1
            move += 1

        next_index = None
        while (move < len(idxDataSet)):
            value = idxDataSet.get(move, None)
            if value:
                next_index = move
                break
            move += 1

        hyper = {
            'index': index,
            'next_index': next_index,
            'page_size': page_size,
            'data': data
        }

        return hyper
