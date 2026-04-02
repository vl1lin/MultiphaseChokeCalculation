import logging
from properties_abc import CalculationProperties


logger = logging.getLogger(__name__)


class CalculationOilProperties(CalculationProperties):
    def __init__(self, *, density_in_api: float,
                 temperature_in_kelvin_in_kelvin: float,
                 pressure: float,
                 specific_gravity_of_gas: float):
        self.density_in_api = density_in_api
        self.specific_gravity_of_oil_by_water = 141.5 / (self.density_in_api + 131.5)
        self.temperature_in_kelvin = temperature_in_kelvin_in_kelvin
        self.pressure = pressure
        self.specific_gravity_of_gas = specific_gravity_of_gas
        self.gas_solubility = self.calculate_gas_solubility()

    def calculate_heat_capacity(self) -> float:
        expression_1 = (0.355 + 0.00176 * self.density_in_api)
        expression_2 = (0.0051 + 1.167 * 10 ** (-5) * self.density_in_api)
        heat_capacity = 778 * (expression_1 + expression_2 * self.temperature_in_kelvin)
        return heat_capacity

    def calculate_gas_solubility(self) -> float:
        expression_1 = self.pressure * self.specific_gravity_of_gas / (self.temperature_in_kelvin + 460)
        expression_2 = 1 / (0.023 * self.specific_gravity_of_oil_by_water ** 3.8)
        gas_solubility = (expression_1 * expression_2) ** 1.17647
        return gas_solubility

    def calculate_volume_coefficient(self) -> float:
        expression_1 = 0.00033 / self.specific_gravity_of_oil_by_water ** 1.8297
        expression_2 = self.temperature_in_kelvin - 60
        expression_3 = 1 - 0.00048 * self.gas_solubility
        oil_volume_coefficient = (1 + expression_1 * expression_2) * expression_3
        return oil_volume_coefficient
