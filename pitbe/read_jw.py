def read_jw(jw_inf):
    read_counter = 0
    circ_counter = 0
    squ_counter = 0
    image_counter = 0
    image_sub_counter = 0
    minus_counter = 0
    plus_counter = 0
    minus_flag = 0
    num_list = []
    sub_num_list = ""
    ope_list = []
    sub_ope_list = ""
    e_sub = ""
    img_ov_zero = ""
    img_ls_zero = ""
    img_e_box = ""
    read_switch_list = ["-", "0", "1", "2", "3", "4",
                        "5", "6", "7", "8", "9"]
    for i in range(len(jw_inf)):
        if jw_inf[i] == "(":
            read_counter = 1
            circ_counter += 1
        elif jw_inf[i] == "[":
            read_counter = 2
            squ_counter += 1
        elif jw_inf[i] == "+":
            read_counter = 3
            plus_counter += 1
            image_counter = 0
            image_sub_counter = 0
        elif jw_inf[i] == "]":
            read_counter = 4
        elif jw_inf[i] == "e":
            read_counter = 5
        elif jw_inf[i] in read_switch_list:
            image_counter = 1
        elif jw_inf[i] == ".":
            image_counter = 0
            image_sub_counter = 2
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
            if circ_counter != squ_counter:
                len_snl = len(img_ls_zero)
                if int(img_ov_zero) < 0:
                    minus_flag = 1
                add_inv_ele = int(img_ov_zero) + float(int(img_ls_zero))/10**(len_snl)*(-1)**(minus_flag)
                if e_sub != "":
                    add_inv_ele *= (10**int(e_sub))
                num_list.append(add_ele*(-1)**minus_counter*1.j)
                e_sub = ""
                img_ov_zero = ""
                img_ls_zero = ""
                plus_counter += 1
                circ_counter += 1
                minus_flag = 0
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
        elif read_counter == 3 and plus_counter % 2 == 0:
            if image_counter + image_sub_counter == 1:
                img_ov_zero += jw_inf[i]
            if image_counter + image_sub_counter == 3:
                img_ls_zero += jw_inf[i]
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
            if jw_inf[i+1] == "j":
                e_switch = 1
            if jw_inf[i+1] == " ":
                e_switch = 1
            if jw_inf[i+1] == "[":
                e_switch = 1
            if e_switch < 1:
                e_sub += jw_inf[i+1]

    return num_list, ope_list
