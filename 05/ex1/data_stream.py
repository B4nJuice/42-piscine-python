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

        return [data for data in data_batch if data == criteria]

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

    def filter_data(
            self,
            data_batch: List[Any],
            criteria: Optional[str] = None) -> List[Any]:
        try:
            crit, high = criteria.split(":")
            high = float(high)
            return [data for data in data_batch if float(
                data.split(":")[1]) >= high and data.startswith(crit)]
        except Exception:
            return super().filter_data(data_batch, criteria)


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

    def filter_data(
            self,
            data_batch: List[Any],
            criteria: Optional[str] = None) -> List[Any]:
        try:
            large_trans: int = int(criteria)
            return [data for data in data_batch if int(
                data.split(":")[1]) >= large_trans]
        except Exception:
            return super().filter_data(data_batch, criteria)


class EventStream(DataStream):
    def __init__(self, stream_id: str, data_type: str) -> None:
        super().__init__(stream_id, "Event Stream", data_type)

    def process_batch(self, data_batch: List[Any]) -> str:
        errors: int = 0

        for data in data_batch:
            try:
                if isinstance(data, str):
                    if data not in ["login", "logout", "error"]:
                        raise ValueError(
                            f"{data} is not supported"
                            )

                    if data == "error":
                        errors += 1
                else:
                    raise ValueError(f"{data} has to be str.")
            except Exception:
                print(f"format error: {data}")

        return f"Event Analysis: {len(data_batch)} events,\
 {errors} error{'s'*(errors > 1)} detected"


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

    print()

    event: EventStream = EventStream(
        "EVENT_001",
        "System Events")
    event_stats: Dict[
        str, Union[str, int, float]] = event.get_stats()

    print(f"Stream ID: {event_stats.get('stream_id')},\
 Type: {event_stats.get('data_type')}")

    event_batch: List[str] = ["login", "error", "logout"]
    print(f"Processing event batch: {event_batch}")

    event_analysis: str = event.process_batch(event_batch)
    print(event_analysis)

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")

    print("Batch 1 Results:")
    mixed_streams: List[tuple[DataStream, List[str]]] = [
        (sensor, ["temp:20.2", "humidity:50"]),
        (transaction, ["buy:100", "sell:50", "buy:20", "sell:10"]),
        (event, ["login", "error"])
    ]

    for stream, data_batch in mixed_streams:
        if isinstance(stream, SensorStream):
            print(f"Sensor data: {len(data_batch)} readings processed")
        elif isinstance(stream, TransactionStream):
            print(f"Transaction data: {len(data_batch)} operations processed")
        elif isinstance(stream, EventStream):
            print(f"Event data: {len(data_batch)} events processed")

    print("\nStream filtering active.")

    print(f"\nFiltering sensor batch: {sensor_batch} with humidity >= 10:")
    print(sensor.filter_data(sensor_batch, "humidity:10"))
    print(f"\nFiltering transaction batch: {transaction_batch} with\
 transaction > 100:")
    print(transaction.filter_data(transaction_batch, "100"))
    print(f"\nFiltering event batch: {event_batch} with \"logout\":")
    print(event.filter_data(event_batch, "logout"))

    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    data_stream()
