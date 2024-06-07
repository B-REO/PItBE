def cont_order(order, rank):
    by_order = format(order, ('0' + str(rank) + 'b'))
    cont_list = []
    for i in range(len(by_order)):
        cont_list.append(int(by_order[i]))
    return cont_list
