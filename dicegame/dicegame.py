from sys import stdin

gunnar = [int(x) for x in stdin.readline().split()]
emma =   [int(x) for x in stdin.readline().split()]


def winner(gunnar, emma):
    gunnar_exp = expectation_value(gunnar[0], gunnar[1], gunnar[2], gunnar[3])
    emma_exp = expectation_value(emma[0], emma[1], emma[2], emma[3])
    print(gunnar_exp, emma_exp)
    if emma_exp == gunnar_exp:
        return "Tie"
    elif gunnar_exp > emma_exp:
        return "Gunnar"
    else:
        return "Emma"

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
    return round(exp_val)

print (winner(gunnar, emma))
