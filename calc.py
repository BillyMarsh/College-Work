
done = False
var1 = ""

def add(number1,number2):
  num = number1 + number2
  print(number1, "+", number2, "=", num)

def subtract(number1,number2):
  num = number1 - number2
  print(number1, "-", number2, "=", num)

def multi(number1,number2):#
  num = number1 * number2
  print(number1, "*", number2, "=", num)

def division(number1,number2):
  if number2 == 0:
    print(number1, "/", number2, "=", "0")
  else:
    num = number1 / number2
    print(number1, "/", number2, "=", num)


def main():
  print ("")
  print ("1) Add")
  print ("2) Subtract")
  print ("3) Multiply")
  print ("4) Divide")
  print ("")
  var1 = input("Enter your option: ")
  cal(var1)
  done = True

def cal(var1):
    if var1 == "1":
      number1 = int(input("Enter your first number to add: "))
      number2 = int(input("Enter your second number to add: "))
      add(number1,number2)
      done = False
      main()
    elif var1 == "2":
      number1 = int(input("Enter your first number to subtract: "))
      number2 = int(input("Enter your second number to subtract: "))
      subtract(number1,number2)
      done = False
      main()
    elif var1 == "3":
      number1 = int(input("Enter your first number to multiply: "))
      number2 = int(input("Enter your second number to multiply: "))
      multi(number1,number2)
      done = False
      main()
    elif var1 == "4":
      number1 = int(input("Enter your first number to subtract: "))
      number2 = int(input("Enter your second number to subtract: "))
      division(number1,number2)
      done = False
      main()
    else:
      done = False
      main()

main()
