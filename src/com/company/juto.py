from Queue import Queue

def better (exp):
    starters = (1,1,1,3)
    m = 10 ** exp
    w = starters
    max_possible_combinations = (m) ** 4 + 4
    cur = 4

    while True:
        next_value = (w[3] + (2*w[1]) % m) % m
        w = w[1:] + (next_value,)
        if w == starters:
            return cur
        if cur > max_possible_combinations:
            print "over done it"
            return -1
        if cur % (max_possible_combinations // 4) == 0:
            print "quarter"
        cur += 1
    # return cur - 4

def generate(exp):
    v = [1,1,1,3]
    m = 10 ** exp
    max_possible_combinations = (m / 2) ** 4 + 4

    for cur in xrange(4, max_possible_combinations):
        v.append((v[cur-1] + (2*v[cur-3]) % m) % m)

    return v

def find_cycle(v):
    comp, cur, num_matched = 0, 4, 0
    while comp != 4:
        if v[cur] == v[comp]:
            comp += 1
        else:
            comp = 0
        cur += 1
