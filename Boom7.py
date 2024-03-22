list_of_num=[1,3,4,49,7,21,28,532,17,27,14,425,45,657,7,4,87,76,57,74,54,75,74,76,65878,698,9987,92,75,75,867,8,78,12,324,67]

def boom_7(list_of_num):
    list_of_num = [str(i) for i in list_of_num]
    for num in list_of_num:
        if int(num) % 7 == 0 or '7' in num:
            print("boom", num)

boom_7(list_of_num)