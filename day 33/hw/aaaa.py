# რა იქნა რამხელა დავალებაა

# append ამატებს არგუმენტს სიის ბოლოს
# pop შლის შემოტანილ ინდექსზე მყოფნ არგუმენტს
# insert ამატებს არგუმენტს შემოტანილ ინდექსზე

ts = ["pmo", 67, 14.88]
print(len(ts))

list=[]
for i in range(5):
  list.append(input("enter num: "))

colors = ["red", "green", "blue", "yellow", "purple"]
colors.pop(4)
print(colors)

animals = ["dog", "cat", "elephant", "lion"]
animals.insert(2,"monkey")
print(animals)


lst=[]
for i in range(3):
  lst.append(input("enter student: "))
lst.append("teacher")
lst.pop(2)
print(len(lst))
print(lst)

# custom ფუნქცია არის ფუნქცია რომელსად შენ თვითონ აკეთბ def ფუნქციით, მას ვიყენებთ რომ გამოვიყენოთ განმეორებადი კოდის ბლოკი უფრო ჩქარად
# ყოველ ჯერზე კოდის გამეორების მაგიერ მხოლოდ ფუნქიის გამოძახება დაგჭირდება
# def func(a,b)
#           ^ პარამეტრები
# func(10,20)
#        ^ არგუმენტი

def sum(a,b):
  return a+b

def EvenOrOdd(num):
  if num ==0:
    return "that's 0"
  elif num%2 == 0:
    return "even"
  else:
    return "odd"
  
def cube(a):
  return a*a

def up(str):
  return str.upper()

def call(nm,lsnm):
  return  "wsp",nm,lsnm

