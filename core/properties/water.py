import logging
from properties_abc import CalculationProperties


logger = logging.getLogger(__name__)


class CalculationWaterProperties(CalculationProperties):
    def __init__(self, pressure: float, temperature_in_kelvin: float):
        self.pressure = pressure
        self.temperature_in_kelvin = temperature_in_kelvin
        self.specific_gravity_of_water = self.calculation_specific_gravity_of_water()

    def calculate_heat_capacity(self) -> int:
        heat_capacity = 778
        return heat_capacity

    def calculate_gas_solubility(self) -> float:
        expression_1 = 0.013 - 3 * 10 ** (-5) * self.temperature_in_kelvin
        expression_2 = 2.8 * 10 ** (-5) * self.pressure ** 1.6
        gas_solubility = expression_1 * self.pressure - expression_2
        return gas_solubility

    def calculation_specific_gravity_of_water(self) -> float:
        expression_1 = 1.366 * 10 ** (-5) * self.temperature_in_kelvin
        expression_2 = 9.503 * 10 ** (-7) * self.temperature_in_kelvin ** 2
        specific_gravity_of_water = 1.004 - expression_1 - expression_2
        return specific_gravity_of_water

    def calculate_volume_coefficient(self) -> float:
        expression_1 = 0.999 / self.specific_gravity_of_water
        expression_2 = 1 * 10 ** (-6) * self.pressure
        water_volume_coefficient = expression_1 - expression_2
        return water_volume_coefficient
