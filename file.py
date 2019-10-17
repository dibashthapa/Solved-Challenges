#Importing datetime module to get date for gettting month,day and year
#In python we have to import modules to access some inbuilt functions and methods
import datetime
#Making user to input date in MM-DD-YYYY format and converting into string with str() function
date=str(input("Enter date:MM-DD-YYYY"))
#Splitting month,day and year by'-' if the input is 12-12-2019 then it will be stored as 
#array like this ['12','12','2019' and storing it in the variable so that we can access it]
x=date.split("-")
#printing array to check no need to print btw
print(x)
#now getting month,day and year from an array x. we know that indexing of an array starts from 0
#so we have 12 in 0 index and 12 in 1 index and 2019 in 2 index and converting into int because we 
#cannot compare string and int
month=int(x[0])
day=int(x[1])
year=int(x[2])

#Now getting date from datetime.date.today() function and datetime will store an integer 
#So it is converted to string to use .split() function
datetime=str(datetime.date.today())
y=datetime.split("-")
#Getting presentyear,month and day
presentyear=int(y[0])
presentmonth=int(y[1])
presentday=int(y[2])
#Checking if the month , day and year is error or not
if(int(month)>12):
    print("There are only 12months in a year.Please check your input")
elif(int(day)>32):
    print("!input error!Days aren't supported. please check")
elif(year>presentyear):
    print("sorry incorrect date!Please Try Again")
else:
    print("Month:",month,"day:",day,"Year:",year)


#we get negative integer if we subtract greater number from smaller number
#So i am using conditions here
if(presentday>day):
    daydif=presentday-day
else:
    daydif=day-presentday
#same here too
if(presentmonth>month):
    monthdif=presentmonth-month
else:
    monthdif=month-presentmonth

yeardif=presentyear-year

#printing the output
print("You are"+str(yeardif-1)+" years old "+str(12-monthdif)+"months",str(30-daydif)+"days")