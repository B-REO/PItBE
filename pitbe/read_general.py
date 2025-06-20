def read_general(jw_inf):
    num_list = []
    ope_list = []
    sub_num_list = ""
    sub_ope_list = ""
    convert_list = []
    ope_con_list = []
    read_counter = 1
    preserve_switch = 0
    for i in range(len(jw_inf)-1):
        if jw_inf[i+1] == "[":
            read_counter = 2
        elif jw_inf[i+1] == "]":
            read_counter = 3
        if read_counter == 1:
            sub_num_list += jw_inf[i]
            preserve_switch = 1
        if read_counter == 2:
            if preserve_switch == 1:
                convert_list.append(sub_num_list)
                sub_num_list = ""
                preserve_switch = 0
            sub_ope_list += jw_inf[i+1]
        if read_counter == 3:
            ope_con_list.append(sub_ope_list)
            sub_ope_list = ""
            read_counter = 4
            countdown = 4
        if read_counter == 4:
            if countdown == 0:
                read_counter = 1
            else:
                countdown -= 1
    for i in range(len(convert_list)):
        if convert_list[i][0] != '(':
            num_list.append(complex(convert_list[i]))
        else:
            convert_list[i] = convert_list[i][1:-1]
            num_list.append(complex(convert_list[i]))
    for i in range(len(ope_con_list)):
        ope_con_list[i] = ope_con_list[i][1:]
        if 0 < len(ope_con_list[i]):
            ope_con_list[i] = ope_con_list[i].replace(" ", "")
        ope_list.append(ope_con_list[i])
        
    return num_list, ope_list
