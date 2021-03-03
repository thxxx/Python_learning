# """
# As you can see, the code is broken.
# Create the missing functions, use default arguments.
# Sometimes you have to use 'return' and sometimes you dont.
# Start by creating the functions
# """

# print("wee")

# def is_on_list(days:list, yoil: str) -> bool:
#     for n in range(0,len(days)):
#         if days[n] == yoil:
#             return True
#     return False

# def get_x(days:list, num: int) -> str:
#     return days[num]

# def add_x(days:list, yoil: str) -> bool:
#     days.append(yoil)

# def remove_x(days:list, yoil: str) -> bool:
#     days.remove(yoil)

# # \/\/\/\/\/\/\  DO NOT TOUCH AREA  \/\/\/\/\/\/\ #

# days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# print("Is Wed on 'days' list?", is_on_list(days, "Wed"))

# print("The fourth item in 'days' is:", get_x(days, 3))

# add_x(days, "Sat")
# print(days)

# remove_x(days, "Mon")
# print(days)


# # /\/\/\/\/\/\/\ END DO NOT TOUCH AREA /\/\/\/\/\/\/\ #



"""
Again, the code is broken, you need to create 4 functions.
  - add_to_dict: Add a word to a dict.
  - get_from_dict: Get a word from inside a dict.
  - update_word: Update a word inside of the dict.
  - delete_from_dict: Delete a word from the dict.

All this functions should check for errors, follow the comments to see all cases you need to cover.

There should be NO ERRORS from Python in the console.
"""

def add_to_dict(dicti: dict, *args:str):
    if type(dicti) != dict:
        print("You need to send a dictionary. You sent:", type(dicti))
    elif len(args) != 2:
        print("You need to send a word and a definition")
    elif args[0] in dicti:
        print( args[0], "is already on the dictionary. Won't add.")
    else :
        dicti[args[0]] = args[1]
        print( args[0], "has been added.")
    
    
def get_from_dict(dicti: dict, search:str=""):
    if type(dicti) != dict:
        print("You need to send a dictionary. You sent:", type(dicti))
    elif not search:
        print("You need to send a word to search for")
    elif search in dicti:
        print(f"{search}: {dicti[search]}")
    else :
        print(f"{search} was not found in this dict.")
    
def update_word(dicti: dict, *args:str):
    if type(dicti) != dict:
        print("You need to send a dictionary. You sent:", type(dicti))
    elif len(args) != 2:
        print("You need to send a word and a definition to update")
    elif args[0] not in dicti:
        print( args[0], "is not on the dict. Can't update non-existing word.")
    else :
        dicti[args[0]] = args[1]
        print( args[0], "has been updated to:", args[1])

def delete_from_dict(dicti: dict, word:str=""):
    if type(dicti) != dict:
        print("You need to send a dictionary. You sent:", type(dicti))
    elif not word:
        print("You need to specify a word to delete.")
    elif word not in dicti:
        print( word, "is not on this dict. Won't delete")
    else :
        del dicti[word]
        print(word,"has been deleted.")


# \/\/\/\/\/\/\ DO NOT TOUCH  \/\/\/\/\/\/\

import os

os.system('clear')


my_english_dict = {}

print("\n###### add_to_dict ######\n")

# Should not work. First argument should be a dict.
print('add_to_dict("hello", "kimchi"):')
add_to_dict("hello", "kimchi")

# Should not work. Definition is required.
print('\nadd_to_dict(my_english_dict, "kimchi"):')
add_to_dict(my_english_dict, "kimchi")

# Should work.
print('\nadd_to_dict(my_english_dict, "kimchi", "The source of life."):')
add_to_dict(my_english_dict, "kimchi", "The source of life.")

# Should not work. kimchi is already on the dict
print('\nadd_to_dict(my_english_dict, "kimchi", "My fav. food"):')
add_to_dict(my_english_dict, "kimchi", "My fav. food")


print("\n\n###### get_from_dict ######\n")

# Should not work. First argument should be a dict.
print('\nget_from_dict("hello", "kimchi"):')
get_from_dict("hello", "kimchi")

# Should not work. Word to search from is required.
print('\nget_from_dict(my_english_dict):')
get_from_dict(my_english_dict)

# Should not work. Word is not found.
print('\nget_from_dict(my_english_dict, "galbi"):')
get_from_dict(my_english_dict, "galbi")

# Should work and print the definiton of 'kimchi'
print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")

print("\n\n###### update_word ######\n")

# Should not work. First argument should be a dict.
print('\nupdate_word("hello", "kimchi"):')
update_word("hello", "kimchi")

# Should not work. Word and definiton are required.
print('\nupdate_word(my_english_dict, "kimchi"):')
update_word(my_english_dict, "kimchi")

# Should not work. Word not found.
print('\nupdate_word(my_english_dict, "galbi", "Love it."):')
update_word(my_english_dict, "galbi", "Love it.")

# Should work.
print('\nupdate_word(my_english_dict, "kimchi", "Food from the gods."):')
update_word(my_english_dict, "kimchi", "Food from the gods.")

# Check the new value.
print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")


print("\n\n###### delete_from_dict ######\n")

# Should not work. First argument should be a dict.
print('\ndelete_from_dict("hello", "kimchi"):')
delete_from_dict("hello", "kimchi")

# Should not work. Word to delete is required.
print('\ndelete_from_dict(my_english_dict):')
delete_from_dict(my_english_dict)

# Should not work. Word not found.
print('\ndelete_from_dict(my_english_dict, "galbi"):')
delete_from_dict(my_english_dict, "galbi")

# Should work.
print('\ndelete_from_dict(my_english_dict, "kimchi"):')
delete_from_dict(my_english_dict, "kimchi")

# Check that it does not exist
print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")

# \/\/\/\/\/\/\ END DO NOT TOUCH  \/\/\/\/\/\/\


