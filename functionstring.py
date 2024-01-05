class FunctionsString:
     def __init__ (self,userinput,shiftnumber):
        self.userinput = userinput
        self.shift_number = shiftnumber
    
     def encryt(self):
        encypted_text = ""
        for char in self.userinput:
            
            if char.isalpha():
               base = ord('A') if char.isupper() else ord('a')
              
               encypted_char = chr((ord(char)- base + self.shift_number ) % 26 + base )
               encypted_text += encypted_char
            else:
               encypted_text += char
        
        return encypted_text


     def decrypt(self,encrypt):
        decrypt_text ="" 
        for char in encrypt:
                if char.isalpha():
                    base = ord('A') if char.isupper() else ord('a')
              
                    encypted_char = chr((ord(char)- base - self.shift_number ) % 26 + base )
                    decrypt_text += encypted_char
                else:
                    decrypt_text += char
        
        print(f"{encrypt} is decrypted to {decrypt_text}")

     def palindromeChecker(self):

        cleaned_input = "".join(c.lower() for c in self.userinput if c.isalnum())
      
        if cleaned_input == cleaned_input[::-1].lower() :
            print(f"{self.userinput} is Palindrom")
        else:
            print(f"{self.userinput} Not a palindrome")   \
            
     def reversestring(self):
        try:           
            reversestring = self.userinput[::-1]
            print(f" the original string is {self.userinput} and reveresed string is {reversestring}")
        except TypeError:
            print("Please enter albhabets only ")