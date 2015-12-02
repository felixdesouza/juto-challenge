def better (exp):
    v = [1, 1, 1, 3]
    m = 10 ** exp
    comp, cur, num_matched = 0,4,0
    while num_matched != 4:
        v.append((v[cur-1] + (2*v[cur-3]) % m) % m)
        if v[cur] == v[comp]:
            comp += 1
            num_matched += 1
        else:
            comp, num_matched = 0,0
        cur += 1
    return cur - 4
