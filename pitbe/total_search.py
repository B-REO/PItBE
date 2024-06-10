import numpy as np


def total_search(ope_list):
    bit_list = []
    app_list = ""
    for i in range(len(ope_list) - 1):
        for j in range(len(ope_list[i+1])-1):
            app_switch = 0
            if ope_list[i+1][j+1] == "X":
                app_switch = 1
            if ope_list[i+1][j+1] == "Y":
                app_switch = 1
            if ope_list[i+1][j+1] == "Z":
                app_switch = 1
            if ope_list[i+1][j+1] == "I":
                app_switch = 1
            if app_switch == 0:
                app_list += str(ope_list[i+1][j+1])
            if app_switch == 1:
                bit_list.append(int(app_list))
                app_list = ""
        bit_list.append(int(app_list))
        app_list = ""
    return np.array(bit_list).max()+1
