# Copied from http://stackoverflow.com/questions/2267362/convert-integer-to-a-string-in-a-given-numeric-base-in-python
def baseN(num,b,numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
    return ((num == 0) and numerals[0]) or (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])

# Will return n if it can be written in just 1s and 0s in base base or the
# next number after that which can be written with just 1s and 0s in that base
def get_next_in_base(n, base):
    radix_form = baseN(n, base)
    # Anything in base 2 can be represented with 1s and 0s! (Opt)
    if base == 2:
        return n

    invalid_index = find_invalid(radix_form)

    if invalid_index == -1:
        return n

    next_valid_index = find_next_valid_index(radix_form, invalid_index)
    if next_valid_index < 0:
        next_valid_index = 0
        old_radix = radix_form
        radix_form = "0" + radix_form

    next_radix_form = radix_form[:next_valid_index] + "1" + "0" * len(radix_form[next_valid_index+1:])
    return int(next_radix_form, base)

def find_invalid(s):
    for i, v in enumerate(s):
        if int(v) > 1:
            return i

    return -1

def find_next_valid_index(s, invalid):
    relevant_portion = s[:invalid]
    reversed_form = relevant_portion[::-1]

    for i, v in enumerate(reversed_form):
        if int(v) == 0:
            return len(reversed_form) - i - 1

    return -1

def get_nearest_for_all(n, base):
    if base == 2:
        return n

    below = get_nearest_for_all(n, base - 1)
    cur = 0
    while (cur != below):
        if cur < below:
            cur = get_next_in_base(below, base)
        else:
            below = get_nearest_for_all(cur, base - 1)
    return cur
