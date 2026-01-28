#!/usr/bin/env python3

from typing import Any, List, Optional, Union, Dict
from abc import ABC, abstractmethod


class DataStream(ABC):

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(
            self,
            data_batch: List[Any],
            criteria: Optional[str] = None) -> List[Any]:
        pass

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        pass
