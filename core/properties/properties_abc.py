import logging
from abc import ABC, abstractmethod


logger = logging.getLogger(__name__)


class CalculationProperties(ABC):
    @abstractmethod
    def calculate_heat_capacity(self) -> float:
        pass

    @abstractmethod
    def calculate_gas_solubility(self) -> float:
        pass

    def calculate_volume_coefficient(self) -> float:
        pass
