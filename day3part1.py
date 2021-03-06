import numpy as np

field = np.zeros( (1000,1000),  dtype=np.int32)

with open("input3.txt","r") as input:
    for line in input:
        stuff = line.split("@")
        name = stuff[0]
        order = stuff[1].split(":")
        start = order[0]
        x = int(start.split(",")[0])
        y = int(start.split(",")[1])
        size = order[1]
        dx = int(size.split("x")[0])
        dy = int(size.split("x")[1])
        for i in range(dx):
            for j in range(dy):
                field[x+i][y+j] += 1

overlap = 0

for i in range(1000):
    for j in range(1000):
        if field[i][j] > 1:
            overlap += 1

print(overlap)
