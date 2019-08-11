import random

import matplotlib.pyplot as plot
import math
import numpy as np

# 扉は1から3の整数の番号が付けられた3枚の扉とする。
# cは車のある扉の番号を表す。
# aはパソコンが無作為に選択した扉の番号を表す。
# mはモンティが開けた扉の番号を表す。
# bはパソコンが扉を変更した場合の変更後の扉の番号を表す。
# changeAndWinは扉を変更した場合の勝ち数
# trialは実験回数

# import monty_function
from monty_function import monty

def monty_1000(num=1000):
    changeAndWin = 0
    trial_list = []
    ratio_list = []

    for trial in range(1, num+1):
        # result = monty_function.monty()
        result = monty()
        c = result["c"]
        a = result["a"]
        m = result["m"]
        b = result["b"]

        if a == c:
            s = "stay"
        else:
            s = "change"
            changeAndWin += 1
        ratio = changeAndWin / trial
        if trial % 100 == 0:
            trial_list.append(trial)
            ratio_list.append(ratio)

    return trial_list, ratio_list

if __name__ == '__main__':
    trial_list, ratio_list = monty_10000()
    for t, r in zip(trial_list, ratio_list):
        print("trial:", t, "change勝率:", '{:.3g}'.format(r))

    plot.plot(trial_list, ratio_list, marker="o", linestyle = "--")
    plot.show()
