import random

import datetime

import matplotlib.pyplot as plot
import numpy as np

def selectFromList(list_):
    size_ = len(list_)
    s = random.randint(0, size_ - 1)
    r = list_[s]
    return r

def selectDate():
    dt1 = datetime.datetime(2019,1,1)
    datedelta_ = random.randint(0, 365)
    dt2 = dt1 + datetime.timedelta(days=datedelta_)
    return dt2

def getDateList(size_):
    list_ = []
    for i in range(size_):
        list_.append(selectDate())
    return list_

def checkDuplicate(list_):
    if len(list_) > len(set(list_)):
        return True
    else:
        return False

def getDupRatio(size_):
    trial_num = 1000
    true_num = 0
    for i in range(trial_num):
        list_ = getDateList(size_)
        result = checkDuplicate(list_)
        if result == True:
            true_num += 1
    ratio = true_num / 1000
    return ratio

    
if __name__ == '__main__':
    n = 0
    size_list = []
    ratio_list = []
    math_list = []

    p1 = 1
    for n in range(1, 51):
        p1 = p1 * (365 - n + 1)/365
        p2 = 1 - p1
        math_list.append(p2)
        ratio = getDupRatio(n)
        print(n, ratio)
        size_list.append(n)
        ratio_list.append(ratio)

    math_np = np.array(math_list) * 100
    ratio_np = np.array(ratio_list) * 100
    plot.plot(size_list, math_np, label="理論値")
    plot.plot(size_list, ratio_np, label="実験結果")
    plot.plot([0, 50], [50, 50], "red", linestyle='dashed')
    # plot.title("誕生日問題実験結果")
    plot.title("The ratio of at least some pair of persons having the same birthday")
    # plot.xlabel("人数(人)")
    plot.xlabel("number of people")
    # plot.ylabel("同じ誕生日の人がいる割合(%)")
    plot.ylabel("having the same birthday ratio")
    plot.legend()
    plot.grid()
    plot.show()
