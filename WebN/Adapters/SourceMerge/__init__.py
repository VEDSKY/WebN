import os
from WebN.Config import Config as WebN
from array import *


class SourceMerge:
    def __init__(self, source_array=None, merge_with=None):
        if merge_with is None:
            merge_with = []
            print(f'[Warning][SourceMerge][No merging output array.]')
        if source_array is None:
            source_array = []
            print(f'[Warning][SourceMerge][Nothing to merge.]')
        self.source_array = source_array
        self.merge_with = merge_with
        self._initialize()

    def _initialize(self):
        print(f'[Info][SourceMerge][Initialized!]')
        self._merge()

    def _merge(self):
        merged = self.source_array + self.merge_with
        print(f'[Info][SourceMerge][Successfully merged][Output: {merged}]')
        return merged
