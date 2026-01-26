from qulacs.gate import X, Y, Z, DenseMatrix, to_matrix_gate


def circ_make(gate_inf, zero_one, circ, qubit, ancilla):
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
            gate_pos = ancilla + tag_num
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
