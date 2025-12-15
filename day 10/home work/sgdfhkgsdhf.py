# < = > <= >=
a= 1<2
b= 2<2
c= 2<3
d= 3<12
e= 12<1

f= 1==1
g= 12==11
h= 100==100
i= 1==0
j= 0==1

q= 1>2
w= 2>2
l= 2>3
k= 3>12
v= 12>1

qw= 129<=21
we= 12<=12
er= 12<=13
rt= 13<=133
ty= 99<=1

af= 1>=11111
sd= 12>=21
df= 90>=99
fg= 75>=100
gh= 100>=75

# logical operations არის True და False-ის შედარება or ან and-ით

abb = True or False
acc = False or False
abc = True or True

vsd = True and True
gss = True and False
hdd = False and False


num = 10
user_num = int(input("enter number: "))

if user_num > num:
    print("your number is greater than 10")
else:
    print("your number is less than 10 or is 10")

name = "Saba"
user_name=input("enter name: ")
if user_name == name:
    print("welcome")
else:
    print("access declined")


certified_age = 18
age = int(input("enter your age: "))
if age < certified_age:
    print("you're not over 18")
else:
    print("Hi, idk")