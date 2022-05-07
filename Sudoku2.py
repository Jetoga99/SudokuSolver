
from numpy import *
import time
def Imp(M):
    if u==1:
        print ("SUDUKU "+str(y)+"X"+str(y)+" RESUELTO")
    else:
        print ("SUDUKU "+str(y)+"X"+str(y)+" SIN RESOLVER")
    M=array(M)
    k=len(M)
    g=sqrt(k)
    l=int(k/g)
    A=[]
    for i in range(l):
        a=g*i
        A.append(a)
    for i in range(k):
        if i in A:
            print (" _"*int(k+k-g))
        for j in range(k):
            if j in A:
                print("|",end="")
            a=M[i][j]
            print (" "+str(a),end="")
            if M[i][j]<=9:
                print (" ",end="")
        print ("|",end="")
        print ("\n")
    print (" _"*int(k+k-g),end="")
    print ()



def PonUnicos(M):
    M2=M
    k=minimo(explora(M2))
    while k[0]==1:
        r=k[1]
        c=k[2]
        b=posibles(M2,r,c)
        M2[r][c]=b[0]
        k=minimo(explora(M2))
    return M2

def minimo(M):
    M2=M
    b=[]
    c=[]
    for i in range(y):
            b=(M2[:,i])
            b1=list(b)
            a=min(b)
            c.append(a)
            
    k=c.index(min(c))
    b=(M2[:,k])
    b1=list(b)
    l=b1.index(min(b1))
    o=min(c)    
    N=[o,l,k]
    return N

def posibles(M,r,c):
    h=M[r,:]
    v=M[:,c]
    k1=(concatenate((h,v),None))
    l=region(M,r,c)
    k=(concatenate((k1,l),None))
    p=[]
    for i in range(1,y+1):
        p.append(i)
    
    m=setdiff1d(p, k)
    return m

def explora(M):
    l=len(M1)
    z=zeros((l,l))+(l+1)

    for o in range(y):
        for p in range(y):
            if M[o,p]==0:
                q=posibles(M,o,p)
                z[o,p]=len(q)
    return z

def region(M,r,c):
    k=sqrt(len(M))
    rr=ceil((r+1)/k)
    cc=ceil((c+1)/k)
    vv=M[int(k*rr-k):int(k*rr),int(k*cc-k):int(k*cc)]
    v=concatenate((vv),axis=0)
    return v

def termino(M):
    k=minimo(M)
    t=(k[0]!=0)
    return t

def gsort(x):
    k=len(x)
    x1=sort(x)
    r=reversed(x1)
    return x1

def Resuelve(M):
    inicio_de_tiempo = float(time.time())
    M1=M
    pag=0
    pila=[]
    borrador=[]
    while termino(M1)==False:
        M1=PonUnicos(M1)
        k=minimo(explora(M1))
        if termino(M1)==True:
            break
        r=k[1]
        c=k[2]
        numeros=posibles(M1,r,c)
        if k[0]!=0:
            borrador.append(borrador)
            borrador.append(M1)
            M1[r,c]=numeros[0]
            numeros=delete(numeros,0)
            g=len(numeros)
            m=zeros((1,((y+1)-g)))
            m=m[0]
            W=()
            W=concatenate((m,g),axis=None)
            otros=gsort(W)
            h=len(borrador)
            pila.append(h)
            pila.append(r)
            pila.append(c)
            concatenate((pila, otros), axis=None)
            concatenate((pila, pila), axis=0)
        else:
            RT= pila[0,:]
            reg=RT[0]
            r=RT[1]
            c=RT[2]
            M1=borrador[:,:,reg]
            numeros=RT[3:len(RT)-1]
            M1[r,c]=numeros[0]
            if numeros[1]==0:
                pila[1,:]
    tiempo_final = float(time.time() )
    tiempo_transcurrido = tiempo_final - inicio_de_tiempo
    print ("\nTomo %f segundos." % (tiempo_transcurrido))
    return M1
print
M=[[3,2,4,0],
[1,4,0,0],
[0,0,1,2],
[2,1,3,4]]          
M=array(M)
M1=array(M)
y=len(M)
u=0
Imp(M1)
M1=Resuelve(M)
u=1
Imp(M1)
print
M=[[3,0,6,5,0,8,4,0,0], 
  [5,2,0,0,0,0,0,0,0], 
  [0,8,7,0,0,0,0,3,1], 
  [0,0,3,0,1,0,0,8,0], 
  [9,0,0,8,6,3,0,0,5], 
  [0,5,0,0,9,0,6,0,0], 
  [1,3,0,0,0,0,2,5,0], 
  [0,0,0,0,0,0,0,7,4], 
  [0,0,5,2,0,6,3,0,0]]
M=array(M)
M1=array(M)
y=len(M)
u=0
Imp(M1)
u=1
M1=Resuelve(M)

Imp(M1)
print
M=[[16, 0, 1, 0, 0, 8, 0, 0, 12, 10, 9, 0, 0, 0, 3, 14],
   [0, 14, 0, 9, 15, 1, 2, 7, 3, 5, 11, 16, 12, 8, 4, 0],
   [4, 0, 0, 7, 0, 3, 10, 16, 0, 2, 0, 0, 5, 0, 9, 0],
   [15, 0, 0, 5, 0, 6, 9, 12, 0, 0, 7, 1, 0, 11, 2, 0],
   [14, 0, 12, 0, 10, 0, 0, 3, 2, 8, 5, 0, 0, 6, 0, 7],
   [7, 0, 5, 8, 0, 11, 0, 14, 0, 0, 4, 0, 0, 16, 10, 0],
   [6, 10, 0, 0, 0, 2, 15, 0, 0, 0, 0, 7, 0, 5, 8, 3],
   [11, 16, 0, 3, 0, 5, 7, 8, 6, 0, 15, 10, 4, 14, 0, 2],
   [1, 0, 15, 0, 16, 0, 0, 2, 0, 12, 8, 4, 10, 3, 0, 5],
   [0, 6, 0, 0, 0, 0, 0, 5, 0, 13, 14, 15, 0, 2, 16, 4],
   [0, 0, 14, 16, 7, 4, 0, 15, 0, 0, 10, 0, 8, 12, 13, 0],
   [3, 13, 4, 10, 0, 12, 1, 0, 16, 6, 2, 5, 14, 7, 15, 11],
   [9, 7, 2, 6, 0, 0, 5, 0, 10, 0, 16, 12, 3, 4, 0, 8],
   [0, 8, 0, 13, 2, 0, 4, 6, 0, 0, 3, 9, 15, 10, 7, 1],
   [0, 4, 3, 14, 12, 15, 8, 0, 0, 0, 1, 2, 0, 9, 5, 16],
   [0, 1, 0, 0, 0, 7, 0, 10, 4, 11, 6, 0, 0, 13, 0, 12]]


M=array(M)
M1=array(M)
y=len(M)
u=0
Imp(M1)
M1=Resuelve(M)
u=1
Imp(M1)

