# i = 10
# while i != -11:
#     print(i)
#     i-=1

# for i in range(1,101):
#     if i%2==0:
#         print(i)

tries = 3
while tries !=0:
    password="GOA123"
    if tries == 3:
        pw=input("enter password: ")
        if pw==password:
            print("acces granted")
            break
        else:
            tries-=1
            print("wrong password! you have 2 tries left")
    elif tries == 2:
        pw=input("enter password: ")
        if pw==password:
            print("acces granted")
            break
        else:
            tries-=1
            print("wrong password! you have 1 try left")
    else:
        pw=input("enter password: ")
        if pw==password:
            print("acces granted")
            break
        else:
            tries-=1
            print("wrong password! GET OUT")