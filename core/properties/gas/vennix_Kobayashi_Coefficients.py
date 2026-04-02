import logging
from dataclasses import dataclass


logger = logging.getLogger(__name__)


@dataclass
class CoefficientValues:
    A1: float = -1.9079137
    A2: float = 0.1859404
    A3: float = 0.6206085
    A4: float = -0.6050965
    A5: float = 0.1390605
    B1: float = 0.7986446
    B2: float = 0.1947895
    B3: float = -0.4916982
    B4: float = 0.4110596
    B5: float = -0.0650830
    D1: float = -0.8398430
    D2: float = -0.5167966
    D3: float = 2.4138572
    D4: float = -1.6793539
    D5: float = 0.3022386
    E1: float = 8.7758015
    E2: float = 0.1733543
    F1: float = 7.2275164
    F2: float = -1.1449913
    G: float = 8.423558
    k: float = 1.394830
    T0: float = -0.774286
    alpha: float = 0.868917
    beta: float = 2.226390
    rho0: float = 0.697342
