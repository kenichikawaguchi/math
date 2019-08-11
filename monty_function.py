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
def selectFromList(list_):
    size_ = len(list_)
    s = random.randint(0, size_ - 1) # リストのインデックスをランダム選択
    r = list_[s]
    return r


def monty():
    list_ = [1, 2, 3] # モンティが扉を選ぶための扉のリスト。
    list2_ = [1, 2, 3] # 最後に変更可能な扉を表すためのリスト。
    c = selectFromList(list_) # 車を扉1〜3のいずれかにランダムに配置する。
    a = selectFromList(list_) # パソコンが扉をランダムに選択する。
    list_.remove(c) # 車のある扉をリストから削除する。
    list2_.remove(a) # パソコンが選んだ扉をリストから削除する。
    if a in list_:
        list_.remove(a) # パソコンが選んだ扉をリストから削除する。
    m = selectFromList(list_) # モンティが開ける扉を選択する。
    list_.remove(m) # モンティが開けた扉をリストから削除する。
    list2_.remove(m)
    b = selectFromList(list2_) # 変える場合の扉を選択する。
    result = {}
    result["c"] = c
    result["a"] = a
    result["m"] = m
    result["b"] = b
    return result

if __name__ == "__main__":
    changeAndWin = 0
    trial_list = []
    changeAndWin_list = []

    for trial in range(1, 11):
        result = monty()
        c = result["c"]
        a = result["a"]
        m = result["m"]
        b = result["b"]

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
