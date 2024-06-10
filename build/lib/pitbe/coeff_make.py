import numpy as np


def coeff_make(vec):
    coeff_list = []
    cal_list = []
    if len(vec) == 2:
        print("You do not need to calculate coefficients!!")
        return [vec[1], vec[0]]
    else:
        for i in range(int(np.log2(len(vec))) - 1):
            pre_list = []
            sep_num = 2**(i+1)
            elelen = len(vec)
            for j in range(sep_num):
                sum_list = vec[elelen//sep_num*j: (elelen//sep_num*(j+1))]
                sum_pow = np.sum(np.array(sum_list)**2)
                if sum_pow == 0:
                    pre_list.append(1)
                else:
                    pre_list.append(sum_pow)
            cal_list.append(pre_list)
        for i in range(len(cal_list)):
            save_list = []
            for j in range(len(cal_list[i])//2):
                save_list.append(np.sqrt(cal_list[i][2*j]/cal_list[i][2*j+1]))
            coeff_list.append(save_list)
        return coeff_list
    