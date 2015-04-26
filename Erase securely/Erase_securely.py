from sys import stdin


numberOfTimesToBeOverwritten = int(stdin.readline())
original = list(stdin.readline())
final = list(stdin.readline())

for times in range(numberOfTimesToBeOverwritten):
    for i in range(len(original)-1):
        if original[i] == '1':
            original[i] = '0'
        else:
            original[i] = '1'



if original == final:
    print("Deletion succeeded")
else:
    print("Deletion failed")

