import random

import matplotlib.pyplot as plot
import sys

TRIAL = 1000
RATIO = 1 / 6

if __name__ == '__main__':
    argvs = sys.argv
    if len(argvs) < 2:
        trial_num = TRIAL
    else:
        trial_num = int(argvs[1])

    trial_list = []
    oneratio_list = []
    one_num = 0
    for i in range(1, trial_num+1):
        dice = random.randint(1, 6)
        if dice == 1:
            one_num += 1
        if i % 10 == 0:
            trial_list.append(i)
            oneratio_list.append(one_num/i)
    plot.plot([1, trial_num], [RATIO, RATIO], "red", linestyle="dashed", label="理論値")
    plot.plot(trial_list, oneratio_list, label="1が出た実験値")
    plot.xlabel("試行回数(回)")
    plot.ylabel("1が出た割合(%)")
    plot.ylim(0, 1)
    plot.legend()
    plot.grid()
    plot.show()
