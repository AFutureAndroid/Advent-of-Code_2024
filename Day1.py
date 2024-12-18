# Day 1 of Advent of Code

f = open("Day1.txt", "r")
list1 = []
list2 = []
test = 0
for line in f:
    line = line.split()
    list1.append(line[0])
    list2.append(line[1])

list1 = sorted(list1)
list2 = sorted(list2)
total = 0
index = 0

for i in list1:
    diff = abs(int(list1[index]) - int(list2[index]))
    total += diff
    index += 1

print(total)

