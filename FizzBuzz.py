def fizzBuzz(number):
    output = ''
    if(number%3 == 0):
        output += "fizz"
    if(number%5 == 0):
        output += "buzz"
    return output