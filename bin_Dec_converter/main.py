#binary-decimal conversor
    
def binary_to_decimal():
    """This function converts binary number
    to decimal and prints it"""
    b_num = input("Enter the binary number: ")
    new_b = b_num[::-1]
    result = 0
    for n in range(0, len(new_b)):
        if new_b[n] == '0':
            continue
        elif new_b[n] == '1':
            result += pow(2,n)
        else:
            print("It seems like you didn\'t enter a binary number")
            break
    print (result)

def decimal_to_binary(num):
    """This function converts decimal number
    to binary and prints it"""
    if num > 1:
        decimalToBinary(num // 2)
    print(num % 2, end='')
    
    
    
    #Putting all together 

n = int(input("ENTER 1 TO CONVERT FROM BINARY TO DECIMAL \nENTER 2 TO CONVERT FROM DECIMAL TO BINARY"))
while n not in [1,2]:
    n = int(input("ENTER 1 TO CONVERT FROM BINARY TO DECIMAL \nENTER 2 TO CONVERT FROM DECIMAL TO BINARY"))
else:
    if n ==1:
        binary_to_decimal()
    else:
        num= int(input("Enter any decimal number: "))
        decimal_to_binary(num)
    