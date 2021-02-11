import random
while True:
    n=int(input('總人數:'))
    m=int(input('一組幾人:'))
    l=n//m#幾組
    r=n%m#剩餘
    arr=[]

    for i in range(n):
        arr.append(i+1)

    arr2 = random.sample(arr, len(arr))#亂序

    for i in range(l):#分組
        arr3=[]
        for j in range(m):
            arr3.append(arr2[0])
            del arr2[0]
        print(arr3)

    arr3=[]#列出剩下的人
    for i in range(r):
        arr3.append(arr2[0])
        del arr2[0]
    print(arr3)
