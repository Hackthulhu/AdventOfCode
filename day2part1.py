def lettercount(string):
    charcount = {}
    for c in string:
        if c in charcount:
            charcount[c] += 1
        else:
            charcount[c] = 1
    return(charcount)

with open("input2.txt", "r") as input:
    count2 = 0
    count3 = 0
    for line in input:
        dict = lettercount(line)
        for key in dict:
            if dict[key] == 2:
                count2 += 1
                break
        for key in dict:
            if dict[key] == 3:
                count3 += 1
                break

    print(count2 * count3)
