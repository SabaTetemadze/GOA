# loop ციკლი არის ერთი კოდის ბევრჯერ გამეორება

# for i in range(5):
#     print("Hi")

# range ფუნქცია ეუბნება for ფუნქციას რამდენჯერ გაიმეოროს შემდეგი კოდი, მაგალითად ეს კოდი 5-ჯერ გამოიყვანს "Hi"-ს


for i in range(100,201):
    print(i)

count = 1
for i in range(21,30):
    if count != 3:
        count+=1
    elif count == 3:
        print(i)
        count =1

for i in range(21):
    if i % 2==0 :
        print(i)


n1 = int(input("enter number: "))
n2 = int(input("enter number: "))
n3 = int(input("enter number: "))
n4 = int(input("enter number: "))
n5 = int(input("enter number: "))
sum =n1+n2+n3+n4+n5
print(sum/5)