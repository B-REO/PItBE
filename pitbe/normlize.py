import numpy as np


def normlize(non_normal, num_anci, num_main):
    nor_list = np.zeros(2**num_main)
    for i in range(len(nor_list)):
        nor_list[i] = non_normal[(2**num_anci)*i]
    return nor_list
