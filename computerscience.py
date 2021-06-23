# id = 2018111111
# name="Bob"
# print(id)
# print(name)
# id=2017147505
# name="김호진"
# print(id)
# print(name)

# print(13*10 + 15/3 - 2)

# print(3**3)

# print(35%3)

# milk_price = 800
# number_of_milks = 3
# print(milk_price*number_of_milks)
# print(milk_price)
# print(number_of_milks)
# milk_price = 1000
# print(milk_price*number_of_milks)
# print(milk_price)
# print(number_of_milks) 

# major = "Computer Science"
# grade = "2"

# print('Bob is Ash\'s friend')

# second_letter = "CHICKEN"[1]

# country = "Republic of Korea"
# print(len(country))
# print(country.lower())
# print(country.upper())
# number = 12345
# print(str(number))

# question_text = "What is your name?"
# answer_text = "My name is Bob"
# full_text = question_text + answer_text
# print(full_text)
# full_text = question_text + " " + answer_text
# print(full_text)

# bool_val1 = 3 != 5
# print(bool_val1)
# bool_val2 = 15 < 10
# print(bool_val2)
# bool_val3 = 15 >= 15
# print(bool_val3)

# bool_one = { -(-(-(-2))) } == -2 and 4 >= 16**0.5 
# print(bool_one)

# bool_two = 2**3 == 108%100 or 'Bob' == 'Robot'
# print(bool_two)

# bool_three = not not False
# print(bool_three)

# if 2 != 4 or 3 < 5:
#  print("The condition is true")

# age = 10
# if age >= 13:
#  print("You can see this movie")
# else:
#  print("“Sorry, you must be 13 or older to watch this movie”")
# age = 15
# if age >= 13:
#  print("“You can see this movie”")
# else:
#  print("“Sorry, you must be 13 or older to watch this movie”")

# gpa = 3.6
# grade = "F"
# if gpa >= 4.0:
#  grade = "A"
# elif gpa >= 3.0:
#  grade = "B"
# elif gpa >= 2.0:
#  grade = "C"
# elif gpa >= 1.0:
#  grade = "D"
# else:
#  grade = "F"
# print(grade)

# shopping_list = ['cola', '‘water’', '‘chicken’', '‘rice’']
# for item in shopping_list:
#  print(item)

# for i in range(5):
#     print("chicken")

# shopping_list = ['cola', '‘water’', 'chicken', '‘rice’']
# print("“Search the chicken”")
# for item in shopping_list:
#  print(item)
#  if item == 'chicken':
#      break
# print("“I found chicken!”")

# ages = [18, 20, 19, 25, 30, 12, 10, 27, 28]
# for age in ages:
#     if age <= 19:
#         continue
#     print(age)

# names = ['Bob', 'Ash', 'Zen', 'Mercy', 'Rein', 'Wins', 'Ana']
# index = 0
# while index < len(names):
#     print(names[index])
#     index += 1

# name = input("Enter your name: ")
# studentID = input("Enter student ID: ")

# print("My name is " + name) # +로 합치면 띄워쓰기가 없다.
# print("My student ID is " + studentID)

# num1 = 300
# num2 = int(input("Enter the value2: "))

# print(num1 - num2)

# string1 = str(input("Enter the string1: "))
# string2 = str(input("Enter the string2: "))
# print(string1 + "+" + string2 + "=" + string1 + string2 )

# my_age = ['Kimhojin', 23]

# grades = [['Bob', 2], ['Ash', 4]]

# my_list = []
# my_list.append(1)
# print(my_list)
# my_list.append(2)
# print(my_list)
# my_list.append(3)
# print(my_list)

# students = ['Bob', 'Ash']
# new_students = students + ['Zen', 'Mercy']
# print(new_students)
# print(students)

# list1 = range(5,10)
# print(list(list1))

# list2 = range(1, 10, 2)
# print(list(list2))

# def introduce_myself():
#     print("Hello Ash.")
#     print("My name is Bob.")
# print("Introduce")
# introduce_myself()

# my_name = input("Type your name...")
# def introduce_myself2(my_name):
#     print("Hello Ash.")
#     print("My name is" + my_name + ".")
# introduce_myself2(my_name)

# friend_name = 'Kwonminjae'
# my_name = 'Kimhojin'
# def introduce_myself3(friend_name, my_name):
#     print("Hello" + friend_name + ".")
#     print("My name is " + my_name + ".")
# introduce_myself3(friend_name, my_name)

# def calculate_age(current_year, birth_year):
#     age = current_year - birth_year
#     return age

# my_age = calculate_age(2019, 2000)
# print("I am " + str(my_age) + " years old.")

# def get_boundaries(target, margin):
#     low_limit = target - margin
#     high_limit = target + margin
#     return low_limit, high_limit
# low, high = get_boundaries(150, 50) #두개를 return하면 순서대로 변수에 들어간다.

# print("Low limit: " + str(low) + ", high limit: " +str(high))


from tkinter import *
from tkinter import scrolledtext
window = Tk()
window.title("FirstGUI")
window.geometry('350x200')
txt=scrolledtext.ScrolledText(window, width=40, height=10)
txt.grid(column=0, row=0)
window.mainloop()
