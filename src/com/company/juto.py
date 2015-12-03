starting_window = (0, 0, 1, 1)

def find_cycle_length(exp):
    # index at which the slow and fast runners meet, this is also the cycle length
    convergence_point_with_window = find_cycle_convergence_point(exp)
    cycle_point = calculate_cycle_point(exp, convergence_point_with_window)
    return cycle_point, convergence_point

def find_cycle_convergence_point(exp):
    slow, fast = 1, 2
    m = 10 ** exp
    slow_window = get_next_window(starting_window, m)
    fast_window = get_next_plus_1_window(starting_window, m)
    print slow_window, fast_window

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
    pass
