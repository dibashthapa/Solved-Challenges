factors=[]
numbers=[]
maximum = int(input(" Please Enter the Maximum Value : "))
for num in range(1, maximum + 1):
    temp = num
    reverse = 0
    while(temp > 0):
        Reminder = temp % 10
        reverse = (reverse * 10) + Reminder
        temp = temp //10
    if(num == reverse):
        numbers.append(num)
print(numbers)
for n in numbers:
    last=n//2
    for nns in range(1,last+1):
        if(n % nns==0):
            no=(n/nns)          
            if(len(str(no))==3 and len(str(nns))==3):
                print(str(no)+"*"+str(nns)+"="+str(n))       
                file=open("dibash.txt","a")
                file.write(str(no)+"*"+str(nns)+"="+str(n)+"\n")
      
#length=len(numbers)-1
#lastNumber=numbers[length]
#for i in range(1,length):
#    if(numbers[i]%i==0):
#        print ( i )
# I have to learn file handling in python 
#First Find all the 

