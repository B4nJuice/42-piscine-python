#!/usr/bin/env python3

from typing import Any, List
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def print_processing(self, data: Any) -> None:
        if type(data) is str:
            data = f"\"{data}\""
        print(f"Processing data: {data}")

    def print_validation(self, data: bool) -> None:
        result: bool = self.validate(data)
        print(f"Validation: {self.type} data {'un'*(not result)}verified")

    def print_output(self, data: Any) -> None:
        result: str = self.process(data)
        output: str = self.format_output(result)
        print(output)

    def format_output(self, result: str) -> str:
        return f"Output: {result}"

    def do_all(self, data: Any) -> str:
        self.print_processing(data)
        self.print_validation(data)
        self.print_output(data)


class NumericProcessor(DataProcessor):
    def __init__(self):
        self.type = "Numeric"
        print("Initializing Numeric Processor...")

    def process(self, data: Any) -> str:

        if self.validate(data):
            size: int = len(data)
            total: int = sum(data)
            avg: float = total / size
            return f"Processed {size} numeric values, sum={total}, avg={avg}"

        return "ERROR"

    def validate(self, data: Any) -> bool:
        if type(data) is not list:
            return False
        for element in data:
            if type(element) is not int:
                return False
        return True


class TextProcessor(DataProcessor):
    def __init__(self):
        self.type = "Text"
        print("Initializing Text Processor...")

    def process(self, data: Any) -> str:

        if self.validate(data):
            size: int = len(data)
            words: List[str] = data.split(" ")
            word_count = len(words)
            return f"Processed text: {size} characters, {word_count} words"

        return "ERROR"

    def validate(self, data: Any) -> bool:
        return type(data) is str


class LogProcessor(DataProcessor):
    def __init__(self):
        self.type = "Log"
        print("Initializing Log Processor...")

    def process(self, data: Any) -> str:

        if self.validate(data):
            output_log: str | None = None
            for log_type in [("ERROR", "ALERT"), ("INFO", "INFO")]:
                log_type, flag = log_type
                if data.startswith(log_type):
                    output_log = data.replace(
                        log_type, f"[{flag}] {log_type} level detected: ",
                        1
                        )
            return f"Processed log: {output_log}"

        return "ERROR"

    def validate(self, data: Any) -> bool:
        if type(data) is not str:
            return False

        for log_type in ["ERROR", "INFO"]:
            if data.startswith(log_type):
                return True

        return False


def stream_processor() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    num_data: List[int] = [1, 2, 3, 4, 5]
    num: NumericProcessor = NumericProcessor()
    num.do_all(num_data)

    print()

    text_data: str = "Hello Nexus World"
    text: TextProcessor = TextProcessor()
    text.do_all(text_data)

    print()

    log_data: str = "ERROR: Connection timeout"
    log: LogProcessor = LogProcessor()
    log.do_all(log_data)

    print("\n=== Polymorphic Processing Demo ===")

    print("\nProcessing multiple data types through same interface...")
    data_list: List[tuple[Any, DataProcessor]] = [
        ([1, 2, 3], num),
        ("Hello World!", text),
        ("INFO: System ready", log)
    ]

    for i, (data, processor) in enumerate(data_list):
        result: str = processor.process(data)
        print(f"Result {i+1}: {result}")

    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    stream_processor()
