import logging
from typing import Final

logger = logging.getLogger(__name__)

_DEFAULT_PRESSURE_DROP_COFF: Final[float] = 0.0


def calculate_q_liq_max(
        p_sn: float,
        t_u: float,
        q_liq: float,
        calc_p_down: bool = False
) -> float:
    logger.info('Начало расчета максимального дебита')
    """
        Рассчитывает максимальный дебит жидкости через штуцер (м³/сут).

        :param p_sn: Давление на устье (или иной параметр, уточни по домену)
        :param t_u: Температура
        :param q_liq_sm3day: Текущий дебит жидкости (см³/сут)
        :param calc_p_down: Режим расчёта. False -> формульный, True -> через calc_choke_q_liq_sm3day
        :return: Максимальный дебит, ограниченный диапазоном [50, 1500]
        """
    if not calc_p_down:
        logger.info("Режим расчета формульный")
        i = -1
        while not (q_liq < 10 ** i):
            i += 1

        threshold = 10.0 ** i
        max_ql = 0.5 * threshold if q_liq < 0.5 * threshold else threshold
    else:
        logger.info("Режим расчета через функцию")
        max_ql = calculate_q_liq_max(p_sn, t_u, _DEFAULT_PRESSURE_DROP_COFF)
    return max_ql
