import numpy as np
from qiskit.quantum_info import Operator
from qiskit.circuit.library import ZGate, XGate, YGate, IGate

def circ_make_for_qiskit(gate_inf, zero_one, circ, qubit, ancilla):
    work_ope_order = []
    input_switch = 0
    input_ele = ""
    if gate_inf == "":
        gate_a = [[1., 0.],
                  [0., 1.]]
        unitary_gate = Operator(np.array(gate_a)).to_instruction()
        for i in range(int(qubit - ancilla)):
            circ.append(unitary_gate, [i])
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
            gate_pos = ancilla + tag_num
            cont_list = []
            for j in range(ancilla):
                cont_list.append(j)
            cont_list.append(gate_pos)
            if work_ope_order[i][0] == "X":
                add_gate = XGate().control(ancilla, ctrl_state=zero_one)
                circ.append(add_gate, cont_list)
            elif work_ope_order[i][0] == "Y":
                add_gate = YGate().control(ancilla, ctrl_state=zero_one)
                circ.append(add_gate, cont_list)
            elif work_ope_order[i][0] == "Z":
                add_gate = ZGate().control(ancilla, ctrl_state=zero_one)
                circ.append(add_gate, cont_list)
            elif work_ope_order[i][0] == "I":
                add_gate = IGate().control(ancilla, ctrl_state=zero_one)
                circ.append(add_gate, cont_list)
                