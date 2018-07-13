# Returns the sum of num1 and num2
def add(var1, var2):
    return var1 + var2


# Returns the result of subtracting var1 - var2
def sub(var1, var2):
    return var1 - var2


# Returns the result of multiplying var1 and var2.
def mul(var1, var2):
    i = 0
    ii = 0
    while i <= var2:
        ii += var1
        i += 1
        if i == var2:
            return ii


# Returns the result of dividing var1 (the dividend) and var2(the divisor)
def div(var1, var2):
    pass
    i = 0
    while var1 >= var2:
        var1 = var1 - var2
        i = i + 1
    print(i)


def exp(var1, var2):
    i = 1
    count = 0
    while count < var2:
        count += 1
        i *= var1
        power = i
        if count == var2:
            print(power)


def modulo(var1, var2):
    i = 0
    while var1 >= var2:
        var1 = var1 - var2
        i = i + 1
    print(var1)


def min_max():
    lst = []
    active = True
    while active == True:
        i = int(input("Enter numbers."))
        h = input("To stop enter 'Stop'. To continue enter 'Continue'")
        lst.append(i)
        if h == 'Stop':
            active = False
        elif h == 'Continue':
            active = True
    ha = sorted(lst)
    print(ha)
    print("The minimum number of this list is " + str(ha[0]))
    print("The maximum number of this list is " + str(ha[-1]))


def bin_octal():
    i = input("Enter a binary number: ")
    [side_a, side_b] = str(i).split(".")
    count = 0
    output1 = ""
    output2 = ""

    if len(side_a) % 3 == 1:
        side_a = side_a + "00"
    elif len(side_a) % 3 == 2:
        side_a = side_a + "0"

    if len(side_b) % 3 == 1:
        side_b = side_b + "00"
    elif len(side_b) % 3 == 2:
        side_b = side_b + "0"

    for index in range(0, len(side_a), 3):
        cur_group = side_a[index: index+3]
        if cur_group == "000":
            output1 = output1 + "0"
        elif cur_group == "001":
            output1 = output1 + "1"
        elif cur_group == "010":
            output1 = output1 + "2"
        elif cur_group == "011":
            output1 = ouput1 + "3"
        elif cur_group == "100":
            output1 = output1 + "4"
        elif cur_group == "101":
            output1 = output1 + "5"
        elif cur_group == "110":
            output1 = output1 + "6"
        elif cur_group == "111":
            output1 = output1 + "7"

    for index in range(0, len(side_b), 3):
        cur_group = side_b[index: index + 3]
        if cur_group == "000":
            output2 = output2 + "0"
        elif cur_group == "001":
            output2 = output2 + "1"
        elif cur_group == "010":
            output2 = output2 + "2"
        elif cur_group == "011":
            output2 = ouput2 + "3"
        elif cur_group == "100":
            output2 = output2 + "4"
        elif cur_group == "101":
            output2 = output2 + "5"
        elif cur_group == "110":
            output2 = output2 + "6"
        elif cur_group == "111":
            output2 = output2 + "7"

        print(output1 + "." + output2)

        count += 3


def bin_hex():
    i = input("Enter a binary number: ")
    [side_a, side_b] = str(i).split(".")
    count = 0
    output1 = ""
    output2 = ""

    if len(side_a) % 4 == 1:
        side_a = side_a + "000"
    elif len(side_a) % 4 == 2:
        side_a = side_a + "00"
    elif len(side_a) % 4 == 3:
        side_a = side_a + "0"

    if len(side_b) % 4 == 1:
        side_b = side_b + "000"
    elif len(side_b) % 4 == 2:
        side_b = side_b + "00"
    elif len(side_b) % 4 == 3:
        side_b = side_b + "0"

    for index in range(0, len(side_a), 4):
        cur_group = side_a[index: index + 4]
        if cur_group == "0000":
            output1 = output1 + "0"
        elif cur_group == "0001":
            output1 = output1 + "1"
        elif cur_group == "0010":
            output1 = output1 + "2"
        elif cur_group == "0011":
            output1 = ouput1 + "3"
        elif cur_group == "0100":
            output1 = output1 + "4"
        elif cur_group == "0101":
            output1 = output1 + "5"
        elif cur_group == "0110":
            output1 = output1 + "6"
        elif cur_group == "0111":
            output1 = output1 + "7"
        elif cur_group == "1000":
            output1 = output1 + "8"
        elif cur_group == "1001":
            output1 = output1 + "9"
        elif cur_group == "1010":
            output1 = output1 + "A"
        elif cur_group == "1011":
            output1 = output1 + "B"
        elif cur_group == "1100":
            output1 = output1 + "C"
        elif cur_group == "1101":
            output1 = output1 + "D"
        elif cur_group == "1110":
            output1 = output1 + "E"
        elif cur_group == "1111":
            output1 = output1 + "F"

    for index in range(0, len(side_b), 4):
        cur_group = side_b[index: index + 4]
        if cur_group == "0000":
            output2 = output2 + "0"
        elif cur_group == "0001":
            output2 = output2 + "1"
        elif cur_group == "0010":
            output2 = output2 + "2"
        elif cur_group == "0011":
            output2 = ouput2 + "3"
        elif cur_group == "0100":
            output2 = output2 + "4"
        elif cur_group == "0101":
            output2 = output2 + "5"
        elif cur_group == "0110":
            output2 = output2 + "6"
        elif cur_group == "0111":
            output2 = output2 + "7"
        elif cur_group == "1000":
            output2 = output2 + "8"
        elif cur_group == "1001":
            output2 = output2 + "9"
        elif cur_group == "1010":
            output2 = output2 + "A"
        elif cur_group == "1011":
            output2 = output2 + "B"
        elif cur_group == "1100":
            output2 = output2 + "C"
        elif cur_group == "1101":
            output2 = output2 + "D"
        elif cur_group == "1110":
            output2 = output2 + "E"
        elif cur_group == "1111":
            output2 = output2 + "F"

        print(output1 + "." + output2)

        count += 4


def bin_dec():
    count = 0
    answer3 = 0
    i = int(input("Enter a binary number to convert to decimal form:"))
    while i > 0:
        length = len(str(i)) - 1
        num1 = 10**length
        i -= num1
        answer3 += 2**length
        count += 1
    print(answer3)


def runOperation(operation, var1, var2):
    # Determines the operation to run based on the operation argument which should be passed in as an integer.
    if operation == 'Add' or operation == '+' or operation == '1':
        print("Adding...")
        print(add(var1, var2))
    elif operation == ('-') or operation == ('Subtract') or operation == ('2'):
        print("Subtracting...")
        print(sub(var1, var2))
    elif operation == ('*') or operation == ('Multiply') or operation == ('3'):
        print("Multiplying...")
        print(mul(var1, var2))
    elif operation == ('/') or operation == ('Divide') or operation == ('4'):
        print("Dividing...")
        print(div(var1, var2))
    elif operation == 'Exponents' or operation == '5':
        print("Calculating...")
        print(exp(var1, var2))
    elif operation == "Minimum and Maximum" or operation == "7":
        print("Going to Minimum/Maximum now...")
        print(min_max())
    elif operation == 'Modulo' or operation == '%':
        print("Calculating...")
        print(modulo(var1, var2))
    elif operation == "Minimum and Maximum" or operation == "7":
        min_max()
    elif operation == "Conversion" or operation == "8":
        hah = input("Would you like to convert binary to decimal, binary to octal, or binary to hexadecimal?")
        if hah == "Binary to Decimal":
            print(bin_dec())
        if hah == "Binary to Octal":
            print(bin_octal())
        if hah == "Binary to Hexadecimal":
            print(bin_hex())
    else:
        print("You must enter a valid operation.")


def main():  # Allows user to run basic program operations with two numbers
    validInput = False
    while not validInput:
        operation = input(
            "What do you want to do? 1. Add, 2. Subtract, 3. Multiply, 4. Divide, 5. Exponents, 6. Modulo, 7. " "Minimum/Maximum, or 8. Conversion. Enter number: ")
        # Get user input
        try:
            var1 = int(input("Enter the first number: "))
            var2 = int(input("Enter the second number: "))
            validInput = True
        except ValueError:
            print("Invalid input. Try again.")
        except:
            print("Unknown error.")

        runOperation(operation, var1, var2)


main()
