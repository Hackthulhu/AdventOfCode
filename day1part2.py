def firsttwice():
    with open("input.txt", "r") as input:
        list = [0]
        dblcheck = True
        flist = []
        for line in input:
            flist.append(int(line))
        while dblcheck:
            for line in flist:
                freq = list[-1] + line
                if freq in list:
                    print("The answer is:"+ str(freq))
                    dblcheck = False
                else:
                    list.append(freq)




if __name__ == "__main__":
    firsttwice()
