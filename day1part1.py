def getval():
    input = open("input.txt", "r")

    res = 0

    for line in input:
        res = res + int(line)

    print(res)

    input.close()

if __name__ == "__main__":
    getval()
