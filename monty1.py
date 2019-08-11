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

changeAndWin = 0
trial_list = []
changeAndWin_list = []

for trial in range(1, 11):
    list_ = [1, 2, 3] # モンティが扉を選ぶための扉のリスト。
    c = random.randint(1, 3) # 車を扉1〜3のいずれかにランダムに配置する。
    a = random.randint(1, 3) # パソコンは扉をランダムに選択する。
    list_.remove(c) # 車のある扉をリストから削除する。
    if c != a: # パソコンが選んだ扉と車のある扉が異なる場合
        list_.remove(a) # パソコンが選んだ扉を削除する。
        m = list_.pop() # 残った扉を選択する。
        b = c # 扉を変更した場合の扉の番号を取得する。
    else: # パソコンが選んだ扉と車のある扉が同じ場合
        idx = random.randint(0, 1) # 残った扉のリストからランダムにindexを選択する。
        m = list_.pop(idx) # 残った扉の番号を取得する。
        b = list_.pop() # 扉を変更した場合の扉の番号を取得する。

    if a == c: # 最初に選んだのが正解の場合
        s = "stay  "
    else: # 変更した場合に正解となる場合
        s = "change"
        changeAndWin += 1
    ratio = changeAndWin / trial
    trial_list.append(trial)
    changeAndWin_list.append(changeAndWin)

    print("車:", c, "選択1:", a, "Monti:", m, "選択2:", b, "正解:", s\
        , "回数:", trial, "changeAndWin:", changeAndWin)

for t, r in zip(trial_list, changeAndWin_list):
    print("trial:", t, "change勝数:", '{:.3g}'.format(r))

plot.plot(trial_list, changeAndWin_list, marker="o", linestyle = "--")
plot.show()
