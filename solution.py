import pandas as pd
import numpy as np


chat_id = 696934164 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    from statsmodels.stats.weightstats import ztest


    alpha = 0.06
    zstat, p_value = ztest(x, value=500, alternative='larger')
    answer = p_value < alpha
    return answer
