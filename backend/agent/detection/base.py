from abc import ABC, abstractmethod


class DetectionRule(ABC):

    name = ""
    severity = "low"

    @abstractmethod
    def detect(
        self,
        system,
        processes,
        connections,
    ):
        pass
