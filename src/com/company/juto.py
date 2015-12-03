starting_window = (0, 0, 1, 1)

def generate(exp):
    v = [1,1,1,3]
    m = 10 ** exp
    max_possible_combinations = (m / 2) ** 4 + 4

    for cur in xrange(4, max_possible_combinations):
        v.append((v[cur-1] + (2*v[cur-3]) % m) % m)

    return v

def find_cycle_length(exp):
    # index at which the slow and fast runners meet, this is also the cycle length
    convergence_point_with_window = find_cycle_convergence_point(exp)
    cycle_point, cycle_point_window = calculate_cycle_point(exp, convergence_point_with_window)
    return convergence_point_with_window[0], cycle_point, cycle_point_window

def find_cycle_convergence_point(exp):
    slow, fast = 1, 2
    m = 10 ** exp
    slow_window = get_next_window(starting_window, m)
    fast_window = get_next_plus_1_window(starting_window, m)

    while slow_window != fast_window:
        slow += 1
        fast += 2
        slow_window = get_next_window(slow_window, m)
        fast_window = get_next_plus_1_window(fast_window, m)

    return slow, slow_window

def get_next_window(window, m):
    return window[1:] + ((window[3] + (2*window[1] % m)) % m,)

def get_next_plus_1_window(window, m):
    temp = get_next_window(window, m)
    return get_next_window(temp, m)

def calculate_cycle_point(exp, point_with_window):
    convergence_point, window = point_with_window
    from_start = starting_window
    m = 10 ** exp
    cur = 0
    while(window != from_start):
        cur += 1
        window = get_next_window(window, m)
        from_start = get_next_window(from_start, m)

    return cur, from_start
