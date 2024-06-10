def vec_make(ele, coflst):
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
