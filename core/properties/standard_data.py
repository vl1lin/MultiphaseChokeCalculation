from dataclasses import dataclass
import logging


logger = logging.getLogger(__name__)


@dataclass
class StandardData:
    def __init__(self, p1_psi, t1_f, gamma_g, gamma_o_api, GOR_scf_stb, WOR_stb_stb):
        # Входные данные
        self.p1 = p1_psi
        self.t1 = t1_f
        self.gamma_g = gamma_g
        self.gamma_o_api = gamma_o_api
        self.GOR = GOR_scf_stb
        self.WOR = WOR_stb_stb

    # Приведённые плотности и молекулярные массы
    # Стандартные условия (STP/STC)
    # Расчёт массовых долей на основе GOR и WOR
    # Критические параметры метана (для уравнения Vennix-Kobayashi)
