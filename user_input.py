def get_numbers(number_count): #defiing function to check if correct value is given
    state = True
    while state: #while loop
        try: #exception handaling
            number = int(input("Please enter the "+number_count+" number:"))
            if number < 0 or number > 255: #if/else loop
                print("Number is not valid enter number between 0-255 only")
            else:
                return number
        except:
            print("Please enter valid integer number")
