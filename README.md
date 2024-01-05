# Math and String Operations

This project includes two modules, `FunctionsMath` for mathematical operations and `FunctionsString` for string operations.

## Table of Contents

- [Description](#description)
- [How to Use](#how-to-use)
  - [Math Problems](#math-problems)
  - [String Problems](#string-problems)
- [Modules](#modules)
  - [FunctionsMath](#functionsmath)
  - [FunctionsString](#functionstring)
- [License](#license)

## Description

The project provides functionalities for mathematical and string operations. It includes modules for solving mathematical problems such as Fibonacci sequence, prime numbers, factorial, and multiplication tables. Additionally, the project offers string-related operations like encryption, decryption, palindrome checking, and string reversal.

## How to Use

### Math Problems

```python
from function import FunctionsMath

# Get user input for a number
numberinput = int(input("Enter a number: "))

# Create an instance of FunctionsMath
function = FunctionsMath(numberinput)

# Perform mathematical operations
function.isOdd()
function.fibonaccisum()
function.print_primes()
function.multiplicationTable()
function.factorialCalculator()
```
### String Problems
```python
from functionstring import FunctionsString

# Get user input for a string
stringinput = input("Enter a string: ")

# Create an instance of FunctionsString
stringFun = FunctionsString(stringinput, 3)

# Perform string operations
stringFun.palindromeChecker()
stringFun.decrypt(stringFun.encryt())
stringFun.encryt()
stringFun.reversestring()
```
FunctionsMath
The FunctionsMath module provides methods for solving various mathematical problems.

isOdd()
Checks if the entered number is odd or even.

fibonaccisum()
Generates the Fibonacci sequence and calculates its sum.

print_primes()
Prints prime numbers up to the entered number.

multiplicationTable()
Prints the multiplication table up to the entered number.

factorialCalculator()
Calculates the factorial of the entered number.

FunctionsString
The FunctionsString module provides methods for performing operations on strings.

encryt()
Encrypts the entered string using a Caesar cipher.

decrypt(encrypt)
Decrypts the given encrypted string.

palindromeChecker()
Checks if the entered string is a palindrome.

reversestring()
Reverses the entered string.
