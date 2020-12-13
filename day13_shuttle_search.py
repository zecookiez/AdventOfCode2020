from time import time

data = [i[:-1] for i in open("input/day13.txt", "r").readlines()]


def chinese_rem_theorem(rem, mod):

    #
    # Solves and finds X for a system of congruences:
    #   X = a_1 (mod n_1)
    #   X = a_2 (mod n_2)
    #   ...
    #   X = a_N (mod n_N)
    #
    # Solutions afterwards can be made by adding/subtracting by MOD
    # Returns X (the initial value), and MOD (the interval where it repeats)
    #
    # Additional Info: https://brilliant.org/wiki/chinese-remainder-theorem/

    def extended_gcd(a, b):
        x, y, u, v = 0, 1, 1, 0
        while a != 0:
            q, r = b // a, b % a
            m, n = x - u * q, y - v * q
            b, a, x, y, u, v = a, r, u, v, m, n
        gcd = b
        return gcd, x, y  # x, y are for [ax + by = gcd]

    a1 = rem[0]
    m1 = mod[0]
    for a2, m2 in zip(rem[1:], mod[1:]):
        gcd, x, y = extended_gcd(m1, m2)
        if a1 % gcd != a2 % gcd:
            raise ValueError("No solutions for given input.")
        _, x, y = extended_gcd(m1 // gcd, m2 // gcd)
        MOD = m1 // gcd * m2
        X = (a1 * (m2 // gcd) * y + a2 * (m1 // gcd) * x) % MOD
        a1 = X
        m1 = MOD
    return a1, MOD


def solve(data):

    # This problem can be solved using the Chinese Remainder Theorem:
    #   - Repeating bus time is the modulo
    #   - The remainder is the time offset
    #
    # Chinese Remainder Theorem in this context:
    #   Solves and finds T (time) for a system of congruences:
    #     T = 0 (mod bus_id_1)
    #     T = 1 (mod bus_id_2)
    #     ...
    #     T = N (mod bus_id_N)

    begin = int(data[0])
    remainder = []
    modulo = []
    best = 1e18, -1

    for ind, bus_id in ((i, int(j)) for i, j in enumerate(data[1].split(",")) if j != "x"):

        remainder.append(-ind)
        modulo.append(bus_id)
        best = min(best, (-begin % bus_id, bus_id))

    return best[0] * best[1], chinese_rem_theorem(remainder, modulo)[0]


t_start = time()

part1, part2 = solve(data)
print("Part 1: %d" % part1)
print("Part 2: %d" % part2)

elapsed = 1000 * (time() - t_start)
print("Time: %.3fms" % elapsed)
