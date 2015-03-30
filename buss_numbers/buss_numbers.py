from sys import stdin

N = stdin.readline()

bus_numbers = [int(x) for x in stdin.readline().split()]

bus_numbers = sorted(bus_numbers)
result = ""
i = 0
while i < (int(N)-4):
    bus0 = bus_numbers[i]
    bus1 = bus_numbers[i+1]
    bus2 = bus_numbers[i+2]
    bus_temp = bus_numbers[i+3]
    if bus2 == bus0+2 and bus1 == bus0+1:
        counter = 4
        while bus_temp == bus2+1:
            bus2 = bus_temp
            bus_temp = bus_numbers[i+counter]
            counter += 1
        i = bus_numbers.index(bus2)+1
        result += (str(bus0)+"-"+str(bus2)+" ")
    else:
        result += str(bus_numbers[i])+" "+str(bus_numbers[i+1])+" "+str(bus_numbers[i+2])
        i = i+3
result =
print (result.strip())
