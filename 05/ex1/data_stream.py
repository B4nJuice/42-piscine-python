#!/usr/bin/env python3

from typing import Any, List, Optional, Union, Dict
from abc import ABC, abstractmethod


class DataStream(ABC):

    def __init__(self, stream_id: int) -> None:
        self.__stream_id: int = stream_id

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


class SensorStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        temps: List[float] = []
        reading_processed = 0

        for data in data_batch:
            try:
                if isinstance(data, str):
                    key, value = data.split(":")
                    if key not in ["temp", "humidity", "pressure"]:
                        raise ValueError(
                            f"key {key} in {data} is not supported"
                            )
                    temps.append(float(value))
                else:
                    raise ValueError(f"{data} has to be str.")
                reading_processed += 1
            except Exception:
                print(f"format error: {data}")

        n_temp: int = len(temps)
        if n_temp == 0:
            avg_temp: str = "undefined"
        else:
            avg_temp: float = sum(temps) / len(temps)

        return f"Sensor Analysis: {reading_processed} readings processed,\
avg temp: {avg_temp:.1f}°C"
