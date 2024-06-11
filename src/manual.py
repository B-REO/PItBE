"""Introduction of PItBE

ある正方行列がパウリ行列「X,Y,Z,I」の積による線型結合で記述できる場合、
その正方行列を線型結合をなす各成分を作用させることで量子回路上で再現する
手法として「ブロックエンコーディング」という手法が存在する。

本プログラム「PItBE」は正方行列を線型結合で表現した際の情報を
入力することで当該行列をブロックエンコーディングした量子回路を
出力するものである。

本プログラムの一部はXANADU社の開発した「PennyLane」というライブラリの
実行結果を分析して作成した。ただあくまでも出力結果を参考にして作成した
のであってコードをそのまま書き写したものではないことは留意して欲しい。

"""

import copy
import numpy as np
from qulacs.gate import X, Y, Z, DenseMatrix, to_matrix_gate


def circ_make(gate_inf, zero_one, circ, qubit, ancilla):
    """circ_make

    この関数は与えられた情報からブロックエンコーディングの
    回路を自動的に組み上げる

    Args:
        gate_inf（list）:
          パウリ行列積の情報が入ったlist
          格納されている各要素はstr型
        zero_one（list）:
          制御ビットの状態に関する情報が記載されているlist
          例えば補助ビット数が5個の回路において
          3番目のゲートへの制御ビットは[1, 1, 0, 0, 0]となる
          格納されている各要素はstr型
          なおこの値は本パッケージ内に含まれている関数
          「cont_order」の出力結果を代入することを想定している
        circ（qulacs_core.QuantumCircuit）:
          組み上げ先の回路
          回路のクラスは「qulacs」に含まれるクラスを利用している
        qubit（str）:
          量子回路に必要な総ビット数（補助ビット+メインビット）
        ancilla（str）:
          量子回路に必要な補助ビット数

    Note:
        前述の通りこの関数には「qulacs」のクラスを一部用いているので
        必ず関数のimport部分で「qulacs」をimportすること
        また引数「zero_list」の値に説明時に触れたもの以外を
        代入した場合想定外の挙動をとる場合もある

    """
    work_ope_order = []
    input_switch = 0
    input_ele = ""
    if gate_inf == "":
        gate_a = [[1., 0.],
                  [0., 1.]]
        for i in range(int(qubit - ancilla)):
            gate = DenseMatrix(int(ancilla + i), gate_a)
            mat_no = to_matrix_gate(gate)
            for j in range(len(zero_one)):
                mat_no.add_control_qubit(len(zero_one) - j - 1, zero_one[j])
            circ.add_gate(mat_no)
    else:
        for i in range(len(gate_inf)):
            if i < len(gate_inf) - 1.5:
                if input_switch > 0.3:
                    work_ope_order.append(input_ele)
                    input_ele = ""
                    input_switch = 0
                if gate_inf[i+1] == "X":
                    input_switch = 1
                if gate_inf[i+1] == "Y":
                    input_switch = 1
                if gate_inf[i+1] == "Z":
                    input_switch = 1
                if gate_inf[i+1] == "I":
                    input_switch = 1
                input_ele += gate_inf[i]
            else:
                work_ope_order.append(input_ele)
                input_switch = 0
                work_ope_order[-1] += gate_inf[-1]
        for i in range(len(work_ope_order)):
            num_inf = ""
            for j in range(len(work_ope_order[i])-1):
                num_inf += work_ope_order[i][j+1]
            tag_num = int(num_inf)
            gate_pos = qubit - tag_num - 1
            if work_ope_order[i][0] == "X":
                gate_a = X(gate_pos)
                mat_no = to_matrix_gate(gate_a)
                for j in range(len(zero_one)):
                    cont_pos = len(zero_one) - j - 1
                    mat_no.add_control_qubit(cont_pos, zero_one[j])
            elif work_ope_order[i][0] == "Y":
                gate_a = Y(gate_pos)
                mat_no = to_matrix_gate(gate_a)
                for j in range(len(zero_one)):
                    cont_pos = len(zero_one) - j - 1
                    mat_no.add_control_qubit(cont_pos, zero_one[j])
            elif work_ope_order[i][0] == "Z":
                gate_a = Z(gate_pos)
                mat_no = to_matrix_gate(gate_a)
                for j in range(len(zero_one)):
                    cont_pos = len(zero_one) - j - 1
                    mat_no.add_control_qubit(cont_pos, zero_one[j])
            elif work_ope_order[i][0] == "I":
                gate_a = [[1, 0],
                          [0, 1]]
                gate = DenseMatrix(int(gate_inf[2*i+1]), gate_a)
                mat_no = to_matrix_gate(gate)
                for j in range(len(zero_one)):
                    cont_pos = len(zero_one) - j - 1
                    mat_no.add_control_qubit(cont_pos, zero_one[j])
            circ.add_gate(mat_no)


def coeff_make(vec):
    """coeff_make

    この関数では本パッケージ内の関数「mat_make」で用いる引数を作成する

    Args:
        vec（list）:
          引数を計算したい要素を格納したlist
          格納されている各要素はfloat型
    
    Returns:
        coeff_list（list）:
          計算結果を格納したlist
          格納されている各要素はfloat型

    """
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


def cont_order(order, rank):
    """cont_order

    この関数は入力値を任意の桁数の2進数表記に変換する

    Args:
        order（str）:
          2進数に変換したい値
        rank（str）:
          2進数表記の際の桁数
    
    Returns:
        cont_list（list）:
          2進数変換後のそれぞれの桁での値を格納したlist
          格納されている値の型はstr

    Examples:
        >>> cont_order(5, 4)
        [1, 0, 1, 0]

    """
    by_order = format(order, ('0' + str(rank) + 'b'))
    cont_list = []
    for i in range(len(by_order)):
        cont_list.append(int(by_order[i]))
    return cont_list


def total_search(ope_list):
    """main_research

    この関数では線形結合を構成するパウリ行列積の一覧から
    量子回路上で必要なビット数を算出する

    Args:
        ope_list（list）:
          パウリ行列積の一覧を記述したlist
          格納されている各要素はstr型
          本パッケージ内にある関数「read_jw」による出力結果を用いる

    Returns:
        np.array(bit_list).max()+1（str）:
          作用先のビット番号のうち最大のものに1を足して出力する
          1を足しているのは作用先のビット番号が0から始まるためである

    Examples:
        >>> main = total_search(ope)
        >>> print(main)
        6

    Note:
        前述の通り入力情報は本パッケージ内の出力結果の利用を
        想定しているので異なる様式を用いた場合望んだ出力結果に
        ならないこともあるので注意してほしい


    """
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


def mat_make(elelist, coeff_lst):
    """mat_male

    この関数では線型結合の係数を補助ビット部分にセットする行列を作成する
    量子回路でもちいる行列はユニタリ性を満たす必要があるので
    複雑な過程が必要だが第一列目の要素と係数さえ入力すれば自動的に作成する
    
    Args:
        elelist（list）:
          作成する行列の第一列目に格納される成分をベクトル要素とするlist
          格納されている要素はfloat型
        coeff_lst（list）:
          関数「vec_nake」でもちいる係数が格納されているlist
          格納されている要素はfloat型

    Returns:
        mat_ele_list（np.array）:
          作成したユニタリ行列が格納されたnp.array
          格納されている要素はfloat型

    """
    mat_ele_list = []
    mat_ele_list.append(elelist)
    for i in range(len(elelist)//2):
        zero_num = i*2
        if np.abs(elelist[i*2]) == 0:
            break
    if elelist[zero_num] != 0:
        zero_num = len(elelist)
    cf_copy = copy.deepcopy(coeff_lst)
    cf_copy.reverse()
    for i in range(len(coeff_lst)):
        adjustor = 0
        mat_copy = copy.deepcopy(mat_ele_list)
        for j in range(len(mat_copy)):
            app_list = vec_make(mat_copy[j], cf_copy[i])
            if i < (len(coeff_lst) - 1.1):
                adjustor = 1
            if np.abs(np.prod(elelist)) == 1:
                adjustor += 1
            if zero_num % 2**(i+2) != 0:
                adjustor += 1
            if adjustor == 3:
                input_ele = 0
                for s in range(2**(i+1) + 2*j):
                    pickup_row_number = (zero_num//(2**(i+2)))*(2**(i+2)) + s
                    input_ele += mat_copy[i][pickup_row_number]**2
                    app_list[pickup_row_number] = 0
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
        mat_ele_list = [[elelist[0], elelist[1]], 
                        [elelist[1], -elelist[0]]]
    return np.array(mat_ele_list)


def normlize(non_normal, num_anci, num_main):
    """normlize

    ブロックエンコーディングによる出力結果は再現した行列を任意の初期状態に
    作用させた結果だけでなく関係のないものも含まれている
    この関数ではその出力結果を入力情報として
    作用結果のみをピックアップし出力させる

    Args:
        non_normal（list）:
          ブロックエンコーディングによる初期状態への作用結果
          格納されている各要素はfloat型である
        num_anci（str）:
          ブロックエンコーディングで用いる補助ビットの数
        num_main（str）:
          ブロックエンコーディングで用いる初期状態を記述するビットの数

    Returns:
        nor_list（list）:
          正しい作用結果のみを格納したlist
          格納されている各要素はfloat型である
          なおlistのsizeはnum_mainのそれである

    Examples:
        >>> result = [0.5, 0.5, 0.5, 0.5]
        >>> norm_res = normlize(result, 1, 1)
        >>> print(norm_res)
        [0.5, 0.5]

    Note:
        本パッケージに含まれている関数「main_research」を用いることで
        引数num_mainは簡単に入力することができる
        ぜひ活用してほしい

    """
    nor_list = np.zeros(2**num_main)
    for i in range(len(nor_list)):
        nor_list[i] = non_normal[(2**num_anci)*i]
    return nor_list


def read_jw(jw_inf):
    """read_jw

    この関数は正方行列のパウリ行列積の線型結合による表現を
    入力情報とし、係数部分と行列積部分に分解し出力するものである

    Args:
        jw_inf（str）: 
          正方行列のパウリ行列の線形結合による表現
          表現については「openfermion」を通じて
          得ることを想定している
        
    Returns:
        num_list（list）:
          線型結合で用いる係数を格納したlist
          各要素はfloat型をとる
        ope_list（list）:
          線型結合で用いるパウリ行列積を格納したlist
          各要素はstr型をとる

    Note:
        前述の通り入力するデータはライブラリ「openfermion」の関数
        「jordan_wigner」による出力結果を想定している
        この手法の出力結果以外を代入した場合、
        正しく実行されないこともあることに注意されたし

    """
    read_counter = 0
    minus_counter = 0
    plus_counter = 0
    num_list = []
    sub_num_list = ""
    ope_list = []
    sub_ope_list = ""
    e_sub = ""
    for i in range(len(jw_inf)):
        if jw_inf[i] == "(":
            read_counter = 1
        elif jw_inf[i] == "[":
            read_counter = 2
        elif jw_inf[i] == "+":
            read_counter = 3
            plus_counter += 1
        elif jw_inf[i] == "]":
            read_counter = 4
        elif jw_inf[i] == "e":
            read_counter = 5
        if read_counter == 1:
            one_counter = 0
            if jw_inf[i+1] == "+":
                one_counter += 1
            if jw_inf[i+1] == "e":
                one_counter += 1
            if jw_inf[i+1] == ".":
                one_counter += 2
            if jw_inf[i+1] == "-":
                one_counter += 3
            if one_counter == 0:
                sub_num_list += jw_inf[i+1]
            if one_counter == 2:
                true_add_num = int(sub_num_list)
                sub_num_list = ""
            if one_counter == 3:
                minus_counter = 1
        elif read_counter == 2:
            sub_switch = 0
            if jw_inf[i+1] == "]":
                sub_switch = 1
            if jw_inf[i+1] == " ":
                sub_switch = 1
            if sub_switch < 1:
                sub_ope_list += jw_inf[i+1]
        elif read_counter == 3 and plus_counter % 2 == 1:
            len_snl = len(sub_num_list)
            add_ele = true_add_num + float(int(sub_num_list))/10**(len_snl)
            if e_sub != "":
                add_ele *= (10**int(e_sub))
            num_list.append(add_ele*(-1)**minus_counter)
            e_sub = ""
            sub_num_list = ""
            read_counter = 0
            minus_counter = 0
        elif read_counter == 4:
            ope_list.append(sub_ope_list)
            sub_ope_list = ""
            read_counter = 0
        elif read_counter == 5:
            e_switch = 0
            if jw_inf[i+1] == "0":
                e_switch = 1
            if jw_inf[i+1] == "+":
                e_switch = 1
            if e_switch < 1:
                e_sub += jw_inf[i+1]
    return num_list, ope_list


def vec_make(ele, coflst):
    """vec_make

    この関数は関数「mat_make」内で行列要素を計算するのに用いる

    Args:
        ele（list）:
          「mat_make」で扱う行列の要素が格納されたlist
          格納されている各要素の型はfloat
        coflst（list）:
          「mat_make」の行列要素に作用させる係数を格納したlist
          格納されている各要素の型はfloat
    
    Returns:
        app_lst（list）:
          計算結果を格納するlist
          格納されている要素はfloat型

    Note:
        この関数は「mat_maker」内のみで用いることを想定している

    """
    app_lst = []
    cor_list_one = []
    cor_list_two = []
    for i in range(len(coflst)):
        corlen = len(ele)//len(coflst)
        cor_list_one = ele[corlen*i: corlen*i+corlen//2]
        cor_list_two = ele[corlen*i+corlen//2: corlen*i+corlen]
        for j in range(len(cor_list_one)):
            app_lst.append(-cor_list_one[j]/coflst[i])
        for j in range(len(cor_list_two)):
            app_lst.append(cor_list_two[j]*coflst[i])
    return app_lst
