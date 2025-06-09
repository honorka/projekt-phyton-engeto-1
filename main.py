"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Silvie Staňková
email: s.zaludova@gmail.com
"""

import sys

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

pocet_textu = len(TEXTS)

# jmeno a heslo

jmena = ["bob","ann","mike","liz"]
hesla = ["123","pass123","password123","pass123"]

jmeno = (input("Your name: "))
heslo = (input("Your password: "))
print("----------------------------------------")
if (jmeno, heslo) not in zip(jmena, hesla):
  print("unregistered user, terminating the program..")
  sys.exit()
  
print("Welcome to the app, ", jmeno)
print("We have",pocet_textu, "texts to be analyzed.")
print("----------------------------------------")


#vyber textu
 
while True:
    vybrany_text = input(f"Enter a number btw. 1 and {pocet_textu} to select: ")
    print("----------------------------------------")
    
    if vybrany_text.isdigit():
        vybrany_text = int(vybrany_text)
        if 1 <= vybrany_text <= pocet_textu:
            break  

    print("Wrong input, try again.") 
  

#pocitani slov
words = (TEXTS[int(vybrany_text) - 1].split())
print(f"There are {len(words)} words in the selected text.")


titlecase_words = 0
for word in words:
  if word.istitle():
    titlecase_words += 1
print(f"There are {titlecase_words} titlecase words.")

uppercase_words = 0
for word in words:
  if word.isupper():
    uppercase_words += 1
print(f"There are {uppercase_words} uppercase words.")

lowercase_words = 0
for word in words:
  if word.islower():
    lowercase_words += 1
print(f"There are {lowercase_words} lowercase words.")

numeric_string = 0
for word in words:
  if word.isnumeric():
    numeric_string += 1
print(f"There are {numeric_string} numeric strings.")

#soucet vsech cisel
numbers = list()
for word in words:
  if word.isnumeric():
    numbers.append(int(word))

sum_all = 0
for number in numbers:
  sum_all += number    
print(f"The sum of all the numbers {sum_all}")
print("----------------------------------------")
print("LEN |   OCCURENCES    |NR. ")
print("----------------------------------------")

#delky slov
word_length = list()
for word in words:
  word_length.append(len(word))

for lenght in range(1,max(word_length)+1):
  print(f"{lenght:<3}", "|","\033[34m",f"{word_length.count(lenght) * '*':<16}","\033[0m",f"{word_length.count(lenght)}")

print("----------------------------------------")
