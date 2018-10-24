import math
import random
def M_colcuate(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)
def D_colculate(Arr):
    M=M_colcuate(Arr)
    D=0
    for ar in Arr:
        D=D+((ar-M)*(ar-M))
    return D/len(Arr)

    # return d*(len(r)/(len(r)-1))
def sko_colculate(Arr):
    D=D_colculate(Arr)
    a=0
    return math.sqrt(D)

def check_ravn(Arr):
    i=0
    counter=0
    while (i<len(Arr)-1):
        if (((Arr[i] ** 2)+(Arr[i+1]**2))<1):
            counter+=1
        i+=2
    return (counter*2)/len(Arr)

def period(seed,A,M):
    RR=[]
    for i in range(2000000):
        seed=get_rand(seed,A,M)
        RR.append(seed/M)
    Xv=RR[2000000-1]
    i1=-1
    i2=-1
    flag=False
    for i in range(len(RR)):
        if(RR[i]== Xv):
            if(flag==False):
                flag=True
                i1=i
                continue
            else:
                i2=i
                break
    per=i2-i1

    i3=0
    while(RR[i3]!=RR[i3+per]):
        i3+=1
    aper=i3+per
    print('Period: '+str(per))
    print('interval: '+str(aper))
def ravnom_ras(a,b):
    ret=a + random.random() * (b - a)
    return ret

def expon(lam):
    return (-1)*math.log(random.random())/lam


def treug(a,b):
    R1=random.random()
    R2=random.random()
    x=a+(b-a)*max(R1,R2)
    return x

def simps(a,b):
    y=ravnom_ras(a/2,b/2)
    z=ravnom_ras(a/2,b/2)
    return y+z

def gaus (n,m,q):
    Rs=0
    for i in range(n):
        Rs=Rs+random.random()
    return m+q*math.sqrt(12/n)*(Rs -n/2)
def gamma (lam,hi):
    temp=1
    for i in range(hi):
        temp=temp*random.random()
    return (-1)*math.log(temp)/lam