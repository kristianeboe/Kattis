from sys import stdin
from math import cos, radians


def lawOfCosines(b, c, angle):
    return (b ** 2 + c ** 2 - 2 * b * c * cos(radians(angle))) ** 0.5


output = 0
# numTestCases = int(stdin.readline())
# for testcases in range(numTestCases):
#     listOfCommands = []
#     numCommands = int(stdin.readline())
#     print(numCommands)
#     for command in range(numCommands):
#         listOfCommands.append(stdin.readline().rstrip('\n'))
#
#     for i in range(numCommands-1):
#         currentCommand = listOfCommands[i]
#         nextCommand = listOfCommands[i+1]
#

# numTestCases = int(stdin.readline())
# for testcases in range(numTestCases):
#     numCommands = int(stdin.readline())
#     output+=int(stdin.readline().split(" ")[1])
#     for command in range(1,numCommands):
#         line = stdin.readline().split()
#         if line[0] == "lt":
#             angle = line[1]
#         elif line[0] == "rt":
#             angle = line[1]

listOfCommands = stdin.read().splitlines()
listOfCommands = listOfCommands[2:]
print(listOfCommands)
output = 100
angle = 120
output = lawOfCosines(output,100,angle)
print(output)
angle = 240
output = lawOfCosines(output,100,angle)
print(output)