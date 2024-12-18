# Code for day 18 of Advent of Code

f = open("Day18.txt","r")

# Start by creating grid
grid = [["." for col in range(5)] for row in range(5)]

test1 = [3,3]


grid[test1[0]][test1[1]] = "#"

# Show final grid
for i in grid:
    print(*i)

