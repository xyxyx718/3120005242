def generate_dict(a,b):
    a_dict = dict()
    b_dict = dict()

    # 生成字典
    for item in a:
        if item in a_dict:
            a_dict[item] += 1
        else:
            a_dict[item] = 1
            b_dict[item] = 0

    for item in b:
        if item in b_dict:
            b_dict[item] += 1
        else:
            b_dict[item] = 1
            a_dict[item] = 0

    return a_dict, b_dict