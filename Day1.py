
f = open("Day1.txt", "r")
list1 = []
list2 = []
for line in f:
    line = line.split()
    list1.append(line[0])
    list2.append(line[1])
    print(list1.size())
    



