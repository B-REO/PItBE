import copy
import numpy as np
from .vec_make import vec_make

def mat_maker(elelist, coeff_lst):
    mat_ele_list = []
    # append the first colum of the desired matrix
    mat_ele_list.append(elelist)
    # search the border between non-zero elements and zero elements
    for i in range(len(elelist)//2):
        zero_num = i*2
        if np.abs(elelist[i*2]) == 0:                
            break
    if elelist[zero_num] != 0:
        zero_num = len(elelist)
    # copy list of coeffcients to use ".reverse()"
    cf_copy = copy.deepcopy(coeff_lst)
    cf_copy.reverse()
    for i in range(len(coeff_lst)):
        # copy elements of matrix, this copy will be append to returned matrix after some process
        mat_copy = copy.deepcopy(mat_ele_list)
        for j in range(len(mat_copy)):
            # calculate non-zero elements of unitary matrix as list
            app_list = vec_make(mat_copy[j], cf_copy[i])
            # append elemnets zero to list of non-zero elements
            if i < (len(coeff_lst) - 1.1):
                if zero_num < (len(elelist) - 0.1):
                    if zero_num%2**(i+2) != 0:
                        input_ele = 0
                        for s in range(2**(i+1) + 2*j):
                            input_ele += mat_copy[i][(zero_num//(2**(i+2)))*(2**(i+2)) + s]**2
                            app_list[(zero_num//(2**(i+2)))*(2**(i+2)) + s] = 0
                        app_list[zero_num] = np.sqrt(input_ele)
                        zero_num += 2
            mat_ele_list.append(np.array(app_list))
    base_mat = [[0, -1], [1, 0]]
    unit = np.eye(2)
    convert = np.kron(unit, base_mat)
    for i in range(len(coeff_lst) - 1):
        convert = np.kron(unit, convert)
    mel_len = len(mat_ele_list)
    if (np.log2(len(elelist)) > 1):
        for i in range(mel_len):
            mat_ele_list.append(np.dot(convert, mat_ele_list[i]))
    if (np.log2(len(elelist)) < 1.1):
        mat_ele_list = [[elelist[0], elelist[1]], [elelist[1], -elelist[0]]]
    return np.array(mat_ele_list).T
    