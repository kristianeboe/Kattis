from sys import stdin

N = stdin.readline()

bus_numbers = [int(x) for x in stdin.readline().split()]
bus_numbers = sorted(bus_numbers)

def join_busnumbers(bus_numbers):
    result = ""
    i = 2
    if int(N) == 1:
        return bus_numbers[0]
    while i < int(N):
        bus0 = bus_numbers[i-2]
        bus1 = bus_numbers[i-1]
        bus2 = bus_numbers[i]

        if bus1 == bus0+1 and bus2 == bus0+2:
            index = i+1
            if index == int(N):
                result+= str(bus0)+"-"+str(bus2)
                break
            while index < int(N) and bus_numbers[index] == bus2+1:
                bus2 = bus_numbers[index]
                index += 1
            result += str(bus0)+"-"+str(bus_numbers[index-1])+" "
            i = index+2
        else:
            result += str(bus0)+" "
            i += 1

    print (i- int(N))
    print (result)
    if i - int(N) == 0:
        return result + str(bus_numbers[i])
    elif i - int(N) == -1:
        return result + str(bus_numbers[i-1])
    elif i - int(N) < -1:
        return result + str(bus_numbers[i-2])+" "+str(bus_numbers[i-1])

print (join_busnumbers(bus_numbers))
