def findHighestNumber(number1, number2, number3):
  numbers = [number1, number2, number3] 

  numbers = max(numbers)

  return(numbers)



number1 = int(input("Enter First Number: "))
number2 = int(input("Enter Second Number: "))
number3 = int(input("Enter Third Number: "))

print("Highest Number is", findHighestNumber(number1, number2, number3))
