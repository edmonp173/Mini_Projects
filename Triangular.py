bac= int(5)
num = 0
num_1 = "* "
sps = " "
while bac != 0:
    bac -= 1
    num += 1
    edmon = num_1 * num
    if num <= 2 or bac == 0:
        print(edmon)
    else:
        num_3=len(edmon) -5
        print("*", sps * num_3,"*")