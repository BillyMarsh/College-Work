number = 1



def checkMod(number):
  if number % 3 == 0 and number % 5 == 0:
      return(number, "FizzBuzz")
  else:
    if number % 3 == 0:
      return(number,"Fizz")
    elif number % 5 == 0:
      return(number, "Buzz")
    else:
      return(number)

    
    
    
  

while number <= 50:
  print(checkMod(number))
  number = number + 1
