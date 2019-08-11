from monty2 import monty_1000

import matplotlib.pyplot as plot
import numpy as np

TRIAL_NUM = 5

if __name__ == '__main__':
    for i in range(TRIAL_NUM):
        trial_list, ratio_list = monty_1000(10000)
        ratio_np = np.array(ratio_list)
        ratio_np = ratio_np * 100
        s = "trial#"+str(i)
        # plot.plot(trial_list, ratio_list, label=s)
        plot.plot(trial_list, ratio_np, label=s)
    plot.plot([0, 1000], [67, 67], "red", linestyle="dashed")
    plot.legend()
    plot.title("モンティ・ホール問題実験結果")
    # plot.xlabel('#_of_trial')
    plot.xlabel('試行回数(回)')
    # plot.ylabel('changeAndWinRatio')
    plot.ylabel('変える場合の正解率(%)')
    plot.ylim(0, 100)
    plot.show()
