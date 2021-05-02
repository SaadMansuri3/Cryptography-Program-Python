class CaesarCipherClass:

    def Encrypt(self,text,key):
        resultText =" "
        for i in range(len(text)):
            letter = text[i]
            if(letter.isupper()):
                if(letter==" "):
                    resultText+=" "
                elif(letter.isdigit()):
                    resultText+=letter
                else:
                    resultText += chr((ord(letter)+key-65)%26+65)
                    
            else:
                if(letter==" "):
                    resultText+=" "
                elif(letter.isdigit()):
                    resultText+=letter
                else:
                    resultText += chr((ord(letter)+key-97)%26+97)
        
        return resultText

    
    def Decrypt(self,text,key):
        resultText =" "
        for i in range(len(text)):
            letter = text[i]
            if(letter.isupper()):
                if(letter==" "):
                    resultText+=" "
                elif(letter.isdigit()):
                    resultText+=letter
                else:
                    resultText += chr((ord(letter)-key-65)%26+65)
            else:
                if(letter==" "):
                    resultText+=" "
                elif(letter.isdigit()):
                    resultText+=letter
                else:
                    resultText += chr((ord(letter)-key-97)%26+97)
        
        return resultText

if(__name__ == "__main__"):
    
    CC = CaesarCipherClass()

    text = "Hello World! 123"
    key = 4
    
    Cipher = CC.Encrypt(text, key)
    print("Cipher Text: "+Cipher)

    print("Plain Text: "+CC.Decrypt(Cipher, key))
