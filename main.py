from function import FunctionsMath
from functionstring import FunctionsString


# Math Problems

numberinput = int(input("Enter number : "))

function = FunctionsMath(numberinput)
function.fibonaccisum()
function.print_primes()
function.multiplicationTable()
function.isOdd()
function.factorialCalculator()


# Strings Problems

stringinput = input("Enter string : ")

stringFun = FunctionsString(stringinput,3)
stringFun.palindromeChecker()
stringFun.decrypt(stringFun.encryt())
stringFun.encryt()
stringFun.reversestring()