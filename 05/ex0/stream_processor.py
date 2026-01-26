#!/usr/bin/env python3

from abc import ABC

class DataProcessor(ABC):
    pass


class NumericProcessor(DataProcessor):
    def process(self, data)