#Crear una función que calcule el mayor de dos números ingresados por el usuario. 
def biggerNumber():
    num1 = float(input("Please enter the first number: "))
    num2 = float(input("Please enter the second number:"))
    
    if(num1 > num2):
        print("The first number is Bigger")
    elif(num2 > num1):
        print("The second number is Bigger")
    elif( num1 == num2 and num2 == num1):
        print("The two numbers are the same")
    else:
        print("Invalided Calculation")

biggerNumber()