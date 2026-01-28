#!/usr/bin/env python3

from typing import Any, List, Optional, Union, Dict
from abc import ABC, abstractmethod


class DataStream(ABC):

    def __init__(
            self,
            stream_id: int,
            stream_type: str,
            data_type: str) -> None:
        self.__stream_id: str = stream_id
        self.__data_type: str = data_type
        print(f"Initializing {stream_type}...")

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(
            self,
            data_batch: List[Any],
            criteria: Optional[str] = None) -> List[Any]:
        pass

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.__stream_id,
            "data_type": self.__data_type
        }


class SensorStream(DataStream):
    def __init__(self, stream_id: str, data_type: str) -> None:
        super().__init__(stream_id, "Sensor Stream", data_type)

    def process_batch(self, data_batch: List[Any]) -> str:
        temps: List[float] = []

        for data in data_batch:
            try:
                if isinstance(data, str):
                    key, value = data.split(":")
                    if key not in ["temp", "humidity", "pressure"]:
                        raise ValueError(
                            f"key {key} in {data} is not supported"
                            )

                    if key == "temp":
                        temps.append(float(value))
                else:
                    raise ValueError(f"{data} has to be str.")
            except Exception:
                print(f"format error: {data}")

        n_temp: int = len(temps)
        if n_temp == 0:
            avg_temp: str = "undefined"
        else:
            avg_temp: float = sum(temps) / n_temp

        return f"Sensor Analysis: {len(data_batch)} readings processed,\
 avg temp: {avg_temp:.1f}°C"


class TransactionStream(DataStream):
    def __init__(self, stream_id: str, data_type: str) -> None:
        super().__init__(stream_id, "Transaction Stream", data_type)

    def process_batch(self, data_batch: List[Any]) -> str:
        net_flow: int = 0

        for data in data_batch:
            try:
                if isinstance(data, str):
                    key, value = data.split(":")
                    if key not in ["buy", "sell"]:
                        raise ValueError(
                            f"key {key} in {data} is not supported"
                            )

                    if key == "buy":
                        net_flow += int(value)
                    elif key == "sell":
                        net_flow -= int(value)
                else:
                    raise ValueError(f"{data} has to be str.")
            except Exception:
                print(f"format error: {data}")

        return f"Trensaction Analysis: {len(data_batch)} operations,\
 net flow: {net_flow:+} units"


def data_stream() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    sensor: SensorStream = SensorStream("SENSOR_001", "Environmental Data")
    sensor_stats: Dict[str, Union[str, int, float]] = sensor.get_stats()

    print(f"Stream ID: {sensor_stats.get('stream_id')},\
Type: {sensor_stats.get('data_type')}")

    sensor_batch: List[str] = ["temp:22.5", "humidity:65", "pressure:1013"]
    print(f"Processing sensor batch: {sensor_batch}")

    sensor_analysis: str = sensor.process_batch(sensor_batch)
    print(sensor_analysis)

    print()

    transaction: TransactionStream = TransactionStream(
        "TRANS_001",
        "Financial Data")
    transaction_stats: Dict[
        str, Union[str, int, float]] = transaction.get_stats()

    print(f"Stream ID: {transaction_stats.get('stream_id')},\
Type: {transaction_stats.get('data_type')}")

    transaction_batch: List[str] = ["buy:100", "sell:150", "buy:75"]
    print(f"Processing transaction batch: {transaction_batch}")

    transaction_analysis: str = transaction.process_batch(transaction_batch)
    print(transaction_analysis)


if __name__ == "__main__":
    data_stream()
