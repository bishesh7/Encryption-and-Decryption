
import random


def makeDict(b,c):
   
    d={}
    i=0
    while i<len(b):
       
        n=random.randrange(len(c))
        d[b[i]]= c[n]
        c=c[:n]+c[n+1:]
        i+=1
    
    return d


    

def encrypt(filename, key):
    import string
    random.seed(key)
    a=string.printable
    b=[]
    i=0
    while i<len(a):
        b+= a[i]
        i+=1

    c=list(b) 

    g=makeDict(b,c)

    f=open(filename)
    msg=f.read()
    
    i=0
    c=''
    while i<len(msg):
        c+=g[msg[i]]
        i+=1
   
    return c

def writeString( msg):
        f=open('encrypt.py.enc','w')
        f.write(msg)
        f.close()

def main():
    key=int(input('enter the key for encryption:'))
    fun=encrypt('groceries.txt', key)
    writeString(fun)

main()
