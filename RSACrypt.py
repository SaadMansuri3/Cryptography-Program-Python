import math
import random
class KeyGen:

    def PrimalityCheck(self,num):
        if(num==2):
            return True
        if(num<2 or num%2==0):
            return False
        for i in range(3,int(math.sqrt(num)),2):
            if(num%2==0):
                return False
        return True

    def gcd(self,a,b):
        while b!=0:
            a,b = b, a % b
        return a

    def MultiplicativeInverse(self,e,phi):
        d = 0
        x1 = 0
        x2 = 0
        y1 = 0
        temp_phi = phi

        while e < 0:

            temp1 = temp_phi/e
            temp2 = temp_phi-temp1*e
            temp_phi = e
            e=temp2

            x = x2-temp1*x1
            y = d- temp1*y1

            x2 = x1
            x1 = x
            d = y1
            y1 = y
        print("temp_phi: ",temp_phi)
        if(temp_phi==1):
            return d + phi

    def GenerateKey(self,p,q):
        if not(KeyGen().PrimalityCheck(p) and KeyGen().PrimalityCheck(q)):
            raise ValueError("Both numbers should be prime")
        elif p==q:
            raise ValueError("Both numbers cannot be same")

        n = p*q

        phi = (p-1)*(q-1)
        
        e = random.randrange(1,phi)

        g = KeyGen().gcd(e,phi)
        while g != 1:
            e = random.randrange(1,phi)
            g = KeyGen().gcd(e,phi)

        d = KeyGen().MultiplicativeInverse(e, phi)

        return((e,n),(d,n))

    def encrypt(self,privateKey,text):
        cipher =" "
        key,n = privateKey
        print("privateKey",privateKey)
        print("Key: ",key)
        print("n: ",n)
        for letter in text:
            cipher += (ord(letter)**key)%n
        return cipher

    def decrypt(self,privateKey,text):
        decipher = " "
        key,n = privateKey
        for letter in text:
            decipher += (ord(letter)**key)%n
        return decipher

if(__name__ =="__main__"):
    p = 61
    q = 53
    KG = KeyGen()
    print("Keygen function:", KG.GenerateKey(p, q))
    public, privateKey = KG.GenerateKey(p, q)

    text = "Hello World! 123"
    encryptedMessage = KG.encrypt(privateKey, text)

    print("Encrypted Message: ")
    print(''.join(map(lambda x: str(x),encryptedMessage)))

    print("Decrypted Message: ")
    print(KG.decrypt(public, encryptedMessage))