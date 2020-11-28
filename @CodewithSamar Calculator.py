# ALL-IN-ONE-CALCULATOR-BY-CodeWithSamar
This is a calculator which will you to do mathematical calculations
import math
import random
import time
print("Welcome to one of the most trusted calculator @codewithsamar calculator")


def add(number1, number2):
    return number1 + number2

def subtract(number1, number2):
  if number1>number2:
      return number1 - number2

  elif number1==number2:
      return number1 - number2

  else:
      return number2 - number1

def multiply(number1, number2):
    return number1 * number2

def divide(number1, number2):
    return number1 / number2

def average(number1, number2):
    return number1 + number2 / 2

def random_number(number1, number2):
     randomnumber = random.randint(number1, number2)
     return randomnumber

def GcD(number1, number2):
    return math.gcd(number1, number2)

def reMainder(number1, number2):
    return math.remainder(number1, number2)

def Power(number1, number2):
    return math.pow(number1, number2)

def LcM(number1, number2):
  gcd  =math.gcd(number1, number2)
  lcm = (number1 * number2) / gcd
  return lcm

print("Enter your choice\n"
      "1. Add\n"
      "2. Subtract\n"
      "3.Multiply\n"
      "4. Divide\n"
      "5. Average\n"
      "6. Random Number\n"
      "7. GCD or HCF \n"
      "8. Remainder \n"
      "9. Power \n"
      "10.LCM  \n")

choice = int(input("What do you want 1, 2, 3, 4, 5, 6, 7, 8, 9, 10: "))

number1 = int(input("Enter first number"))
number2 = int(input("Enter second number"))

if choice == 1:
    print(number1, "+", number2, "=",
          add(number1, number2))
    time.sleep(3)

elif choice == 2:
    print(number1, "-", number2, "=",
          subtract(number1, number2))
    time.sleep(3)

elif choice == 3:
    print(number1, "*", number2, "=",
          multiply(number1, number2))
    time.sleep(3)

elif choice == 4:
    print(number1, "/", number2, "=",
          divide(number1, number2))
    time.sleep(3)

elif choice == 5:
    print("the average of",  number1, "and", number2,  "is =",
          average(number1, number2))
    time.sleep(3)

elif choice == 6:
    print("The Random Number between", number1, "and", number2, "=",
          random_number(number1, number2))
    time.sleep(3)

elif choice == 7:
    print("The GCD of", number1, "and", number2, "=",
          GcD(number1, number2))

elif choice == 8:
    print("The Remainder of", number1, "and", number2, "=",
          reMainder(number1, number2))

elif choice == 9:
    print(number1, "raised to power", number2, "=",
          Power(number1, number2))

elif choice == 10:
    print("The LCM of", number1, "and", number2, "=",
          LcM(number1, number2))


else:
    print(".......ERROR")
