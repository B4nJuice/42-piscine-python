#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, Protocol


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        pass


class ProcessingPipeline(ABC):
    @abstractmethod
    def process(self, data: Any) -> Any:
        pass

    def add_stage(self, stage: ProcessingStage):
        if self.stages is None:
            self.stages = []
        self.stages.append(stage)


class InputStage:
    def process(self, data: Any) -> Any:
        if data is None:
            raise ValueError("Received empty data.")
        return data


class TransformStage:
    def process(self, data: Any) -> Any:
        pass


class OutputStage:
    pass
