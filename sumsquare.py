#finding the sum of squares of first ten natural number
firstSum=0
for i in range(1,101):
    firstSum=firstSum+(i**2)

print(firstSum)
#finding the square of the sum of first ten natural number is
secondSum=0
for i in range(1,101):
    secondSum=secondSum+i

print(secondSum)
difference=(secondSum**2)-firstSum
print(difference)
