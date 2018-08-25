# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 11:18:07 2018

@author: shurastogi
"""
import numpy as np
class Cipher:
    #static varible between 1 and 50 
    static_variable=np.random.randint(1,51,1)
    special_char={'-',',',';','%','#'}
    def __init__(self):
        #constructor functiona to take input
        self.user_string=input("Please enter the text to be encrypted:")
    
    #function to encrypt user input string
    def encrypt(self):
        cipher=''
        string=self.user_string
        for x in range(len(self.user_string)):
            if string[x]==' ':
                yield cipher
            elif (string[x] in self.special_char):
                continue
            elif string[x].isupper():
                cipher= cipher + chr((ord(string[x]) + self.static_variable - 65) % 26 + 65)
                yield cipher
            else:
                cipher = cipher + chr((ord(string[x]) + self.static_variable - 97) % 26 + 97)
                yield cipher
        
    #function to decrypt the encrypted text    
    def decrypt(self,encrypted_text):
        decipher=''
        string=encrypted_text
        for x in range(len(string)):
            if string[x]==' ':
                decipher=decipher+string[x]
            elif (string[x] in self.special_char):
                continue
            elif string[x].isupper():
                decipher= decipher + chr((ord(string[x]) - self.static_variable - 65) % 26 + 65)
            else:
                decipher = decipher + chr((ord(string[x]) - self.static_variable - 97) % 26 + 97)
        print("The decrypted text is {}".format(decipher))

        
        

#object creation for cipher
ci=Cipher()
encr_text=ci.encrypt()
encry=''
decry=''
for x in encr_text:
    encry=x
print("The encrypted text is {}".format(encry))
decr_text=ci.decrypt(encry)