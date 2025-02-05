def read_jw(jw_inf):
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
