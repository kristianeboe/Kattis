from sys import stdin

highScore = 0
counter = 0
winner = 0
for line in stdin:
    counter += 1
    points = sum(map(int, (line.split(" "))))
    if points > highScore:
        highScore = points
        winner = counter

print(winner, highScore)