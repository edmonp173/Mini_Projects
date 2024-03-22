def decimal_to_bin(decimal):
    result =""
    while decimal != 0:
        result = str(decimal % 2) + result
        decimal = (decimal // 2)
    return result


def binary_to_dec(number):
    result = 0
    num = 0
    for i in reversed(str(number)):
        result += int(i) * (2 ** num)
        num += 1
    return result

def ip_decimal_to_binary(ip_address):
    ip_address_list = ip_to_list(ip_address)
    result = ""
    for octet in ip_address_list:
        if result == "":
            result = decimal_to_bin(int(octet))
        else:
            result = result + "." + decimal_to_bin(int(octet))
    return result
    #transform thr decimal list into binary
    #chech for objects ehit less then 8 characters

def ip_to_list(ip_address):
    ip_list= list(ip_address.split("."))
    return ip_list
    #
def decimal_to_8bit_binary(dec_num):
    if 0 <= dec_num <= 255:
        bin_num = desimal_binary.decimal_to_binary(dec_num)
        while len(bin_num) < 8:
            bin_num = "0" + bin_num
        return bin_num
    else:
        print("error")
    #the 8 bit binary




if __name__ == "__main__":
    print(ip_decimal_to_binary("123.45.65.32"))