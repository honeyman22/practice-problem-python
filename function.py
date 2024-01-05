class FunctionsMath:
     def __init__ (self,userinput):
        self.userinput = userinput
    
     def isOdd(self):
        try:           
            if(self.userinput%2==0):               
                print(f"The entered number : {self.userinput} is Even. ")
            else:
                print(f"The entered number : {self.userinput} is Odd. ")    
        except TypeError:
            print("Please enter number only. ")
    
     def fibonaccisum(self):
            nthterm = [0, 1]
            for x in range(2, self.userinput):
               num = nthterm[-1] + nthterm[-2]
               nthterm.append(num)
            total_sum = sum(nthterm)
            print(f"The nth term is {nthterm.pop()}")
            print(f"The sum is {total_sum}")

    
     def factorialCalculator(self):
        result = 1

        for x in range(1 , int(self.userinput) + 1):
            result = (result * x) 
                    
        print(result)   

    
     def print_primes(self):
        for x in range(2, int(self.userinput) + 1):
            is_prime = True
            for y in range(2, int(x**0.5) + 1):
                if x % y == 0:
                    is_prime = False
                    break
            if is_prime:
                print(x)
    

     def multiplicationTable(self ):
        for x in range(1,int(self.userinput)+1):
              row = "\n".join(f"{x} * {y} = {x*y}" for y in range(1, 11))
              print(row)
               
           