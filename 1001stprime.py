upper=120000
lower=1
primenumbers=[]
print("Prime numbers between",lower,"and",upper,"are:")
for num in range(lower,upper+1):
    if(num>1):
        for i in range(2,num):
            if(num%i==0):
                break
        else:
            primenumbers.append(num)
print(primenumbers)
print(len(primenumbers))
print(primenumbers[10000])