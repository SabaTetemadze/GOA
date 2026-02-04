numberius = int(input("enter the goddang number: "))

count = numberius
result = 1
for i in range(1,numberius+2):
    if count == 0:
        print(result)
    else:
        result *= i
        count-=1


num = int(input("AAAAAAAAA: "))
for i in range(2,num):
    if num%i==0:
        print(i)