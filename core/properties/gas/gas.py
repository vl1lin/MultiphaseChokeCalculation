import logging
from vennix_Kobayashi_Coefficients import CoefficientValues


logger = logging.getLogger(__name__)


class CalculationGasProperties:
    def __init__(self, reduced_density: float,
                 reduced_temperature_in_kelvin: float,
                 standard_density: float,
                 standard_temperature_in_kelvin: float):
        self.reduced_density = reduced_density
        self.reduced_temperature_in_kelvin = reduced_temperature_in_kelvin
        self.standard_density = standard_density
        self.standard_temperature_in_kelvin = standard_temperature_in_kelvin

    def calculation_compressibility_factor(self):
        pass
