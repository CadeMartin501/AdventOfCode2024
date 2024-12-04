left = []
right = []

with open("nums.txt") as file:
    lines = file.readlines()

difference = 0

for line in lines:
    line = line.strip().split()
    left.append(int(line[0]))
    right.append(int(line[1]))

left = sorted(left)
right = sorted(right)

for i in range(len(left)):
    difference += abs(left[i] - right[i])

print(difference)

total = 0

for i in range(len(left)):
    j = int(left[i])
    total += (j * right.count(j))

print(total)