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


def invert(d):
    b=[]
    c=[]
    for key in d:
        b+=[key]
        c+=[d[key]]
    n={}
    for value in b:
        n[c[b.index(value)]]=value
    if len(n)<len(d):
        return None
    else:
        return n


def decrypt(filename, key):
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
    inverted=invert(g)

    f=open(filename)
    msg=f.read()
    i=0
    c=''
    while i<len(msg):
        c+=inverted[msg[i]]
        i+=1

    return c

def writeString( msg):
        f=open('decrypte.txt','w')
        f.write(msg)
        f.close()

def main():
    key=int(input('enter the key:'))
    done=decrypt('groceries.txt',key)
    writeString(done)

main()

















