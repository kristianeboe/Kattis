from sys import stdin

N = stdin.readline()

bus_numbers = [int(x) for x in stdin.readline().split()]
bus_numbers = sorted(bus_numbers)

def join_busnumbers(bus_numbers):
    result = ""
    if int(N) == 1:
        return result + str(bus_numbers[0])
    i = 0
    while i < int(N):
        if i < int(N)-2 and bus_numbers[i+2] == bus_numbers[i+1]+1 and bus_numbers[i+1] == bus_numbers[i]+1:
            counter = 3

            while i+counter < int(N) and bus_numbers[i+counter] == bus_numbers[i+counter-1]+1:
                counter += 1
            result += str(bus_numbers[i])+"-"+str(bus_numbers[i+counter-1])+" "
            i = i+counter
        else:
            result += str(bus_numbers[i])+ " "
            i += 1
    return result.strip()

print (join_busnumbers(bus_numbers))
