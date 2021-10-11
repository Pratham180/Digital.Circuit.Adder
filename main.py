import adder #importing adder module
import converter  #importing converter module
import user_input #importing user input module

print("WELCOME TO 8 BIT ADDER CIRCUIT") # printing welcome message
def process_start(): 
    a = user_input.get_numbers("1st")
    b = user_input.get_numbers("2nd")
    if a + b > 255: #if else loop
        print("8 bit adder can not sum value greater than 255")
    else:
         first_binary = converter.decimal_to_binary(a)
         second_binary = converter.decimal_to_binary(b)
         print("Results:")
         print(str(a) + " in binary: " + converter.list_to_string(first_binary)) #printing first number into binary
         print(str(b) + " in binary: " + converter.list_to_string(second_binary)) #printing second number into binary
         result = adder.bit_adder(first_binary, second_binary)
         # printing binary sum
         print("Binary Addition: " + converter.list_to_string(first_binary) + " + " + converter.list_to_string(second_binary) + " = " + converter.list_to_string(result))
         #printing decimal sum
         print("Decimal Addition: " + str(a) + " + " + str(b) + " = " + converter.binary_to_decimal(result))


if __name__ == '__main__': #if loop
    state = True
    process_start()
    while state: #while loop
        c = input("Press 'Y' to continue or 'N' to quit:")
        if c == "y" or c == "Y": #if else loop
            process_start()
        elif c == "n" or c == "N":
            state = False
            print("BYE!")
