def decimal_to_binary(number): #definig function to convert decimal to binary
    binary = []
    while number >= 1:
        if number % 2 == 0: #if else loop
            binary.append(0)
        else:
            binary.append(1)
        number = number // 2
    while len(binary) < 8: #while loop
        binary.append(0)
    return binary[::-1]


def binary_to_decimal(binary): #defining funtion to convert binary to decimal
    decimal = 0
    place = 1
    for i in range(len(binary) - 1, -1, -1): #for loop
        decimal = decimal + binary[i] * place
        place = place * 2
    return str(decimal)


def list_to_string(input_seq): #definig function to convert lost top sting
    final_str = ""
    for i in input_seq: #for loop
        final_str = final_str + str(i)
    return final_str
