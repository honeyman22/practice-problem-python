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
