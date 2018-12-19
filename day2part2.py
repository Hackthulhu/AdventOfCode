def strchardiff(str1, str2):
    strOne = list(str1)
    strTwo = list(str2)
    diff = 0
    positions=[]
    for x in range(1, len(strOne)):
        if strOne[x] != strTwo[x]:
            diff += 1
            positions.append(x)
    return(diff, positions)

def day2part2():
    result =""
    with open("input2.txt","r") as inputone:
        for boxOne in inputone:
            with open("input2.txt","r" )as inputtwo:
                for boxTwo in inputtwo:
                    res, pos = strchardiff(boxOne, boxTwo)
                    if res == 1:
                        str = list(boxOne)
                        del str[pos[0]]
                        for c in str:
                            result += c
    return(result)



answer = day2part2()
print(answer)
