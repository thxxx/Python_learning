"""
As you can see, the code is broken.
Create the missing functions, use default arguments.
Sometimes you have to use 'return' and sometimes you dont.
Start by creating the functions
"""

print("wee")

def is_on_list(days:list, yoil: str) -> bool:
    for n in range(0,len(days)):
        if days[n] == yoil:
            return True
    return False

def get_x(days:list, num: int) -> str:
    return days[num]

def add_x(days:list, yoil: str) -> bool:
    days.append(yoil)

def remove_x(days:list, yoil: str) -> bool:
    days.remove(yoil)

# \/\/\/\/\/\/\  DO NOT TOUCH AREA  \/\/\/\/\/\/\ #

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

print("Is Wed on 'days' list?", is_on_list(days, "Wed"))

print("The fourth item in 'days' is:", get_x(days, 3))

add_x(days, "Sat")
print(days)

remove_x(days, "Mon")
print(days)


# /\/\/\/\/\/\/\ END DO NOT TOUCH AREA /\/\/\/\/\/\/\ #






