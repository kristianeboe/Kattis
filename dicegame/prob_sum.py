from sys import stdin

gunnar = [int(x) for x in stdin.readline().split()]
emma   =   [int(x) for x in stdin.readline().split()]

die1_min = 1
die1_max = 10
die1_sides = 10

die2_min = 2
die2_max = 5
die2_sides = 4


def expectation_value(die1_min, die1_max, die2_min, die2_max):
    sums = {}
    for a in range(die1_min, die1_max+1):
        for b in range(die2_min, die2_max+1):
            if a+b not in sums:
                sums[a+b] = 1
            else:
                sums[a+b] += 1
    prob = 1/(die1_max-die1_min+1)*1/(die2_max-die2_min+1)
    exp_val = 0
    for key in sums:
        exp_val += key*prob*sums[key]

    return exp_val

print (expectation_value(die1_min, die1_max, die2_min, die2_max))
