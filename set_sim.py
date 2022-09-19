def jaccard_similarity(A: set, B: set):
    # 求集合 A 和集合 B 的交集
    nominator = A.intersection(B)
    # 求集合 A 和集合 B 的并集
    denominator = A.union(B)
    # 计算比率
    similarity = len(nominator)/len(denominator)
    return similarity
