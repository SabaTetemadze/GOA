# type() ფუნქცია აბრუნებს თავის ატრიბუტის ტიპს, მაგალიტად:
q = "apple"
w = 123

e = type(q) # ეს ფუნქცია გამოიტანს <class 'str'>
r = type(w) # ეს ფუნქცია გამოიტანს <class 'int'>

# data covertaion არის ფუნცია რომელსაც შეუძლია ცვლადის მნიშვნელობის ტიპის შეცვლა მაგალითად:

t = "30"
c = int(t) # c = 30

y = 25
u = str(y) # u = "25"

i = 33
o = float(i) # o = 33.0


# a = input()
# s = input()
# d = input()
# print (int(a)+int(s)+int(d))
# print(a)
# print(s)
# print(d)



name = input("enter your name: ")
count = int(input("enter a  number: "))
for i in range(count):
    print(name)