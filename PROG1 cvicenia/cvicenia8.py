# ------ Cast prva ------
# Vyrieste vsetky ulohy zo sekcie 8.13 v knihe
# Exercise 8.1
# Read some shit [x]

# Exercise 8.2
# print('banana'.count('a'))

# Exercise 8.3
# is_palindrome = lambda word: word == word[::-1]
# print(is_palindrome('noon'))
# print(is_palindrome('moon'))

# Exercise 8.4
# Cielova funkcionalita: Zistit ci retazec obsahuje aspon jedno male pismeno.
# any_lowercase1: Iteruje vsetky pismenka v retazci a ak dane pismenko 
#                 je male, tak funkcia vrati True, v opacnom pripade vrati 
#                 False. Podotykam, ze for-cyklus vo funkcii je redundantny 
#                 totiz cyklus v ziadnom pripade sa nedostane dalej od prvej
#                 iteracie, kedze po if podmienke funkcia okamzite vrati 
#                 hodnotu True ak preve pismeno retazca je male a False ked 
#                 je velke. Tato funkcia nesplna cielove podmienky.
# any_lowercase2: Iteruje vsetky pismenka v retazci a potom sa rozhoduje o
#                 konstantnom charaktere 'c' ci je male alebo velke pimenko. 
#                 Nasledovne funkcia vracia hodnotu True. Tato funkcia nesplna 
#                 cielove podmienky.
# any_lowercase3: Iteruje vsetky pismenka v retazci, potom vytvara premennu 
#                 v ramci for-cyklu, kde uklada boolean hodnotu ci je aktualne 
#                 pismeno male alebo velke. Na konci vrati hodnotu premennej, 
#                 ktore bolo vytvorene na urovni for-cyklu co by v pythone nemalo 
#                 vadit, ale aj tak je to sketchy. Na koniec funkcia i tak nesplna 
#                 cielove podmienky lebo vracia len hodnotu posledneho pismenka.
# any_lowercase4: Deklaruje premennu "flag" s hodnotou False. Nasledovne iteruje 
#                 vsetky pismenka v retazci a v tele cyklu obnovi hodnotu premennej 
#                 "flag" na logicky sucet, teda OR hodnoty "flag" a hodnoty pismenka 
#                 ci je male alebo velke. Uplatnuje sa zakon agresivnej jednotky, 
#                 preto akonahle .islower() vrati True flag sa zmeni na True a 
#                 ostava v tom stave az do konca funkcie. A to znamena, ze tato 
#                 funkcia splna cielove podmienky.
# any_lowercase5: Iteruje vsetky pismenka v retazci az kym sa najde velke 
#                 pismeno, funkcia vrati hodnotu False a ak sa nenajde ziadne velke 
#                 pismeno vracia hodnotu True. Tato funkcia nesplna cielove podmienky.

# Exercise 8.5
# def rotate_word(word, amount):
#   # One-liner
#   # return "".join([chr(ord(l) + amount) for l in word])
#   nw = ''
#   for l in word:
#     nw += chr(ord(l) + amount)
#   return nw

# print(rotate_word('HAL', 1))


# ------ Cast druha ------
# ------- Uloha 1 -------
# Precitajte si kapitolu 9.1 z knihy. [x]

# ------- Uloha 2 -------
# Vyrieste vsetky ulohy z kapitoly 9.2. 
# Exercise 9.1
# with open('words.txt', 'r') as words:
#   for line in words:
#     word = line.strip()
#     if len(word) > 20:
#       print(f"|{word}|  len={len(word)}")


# Exercise 9.2
# def has_no_e(word):
#   return word.count('e') == 0

# total_words = 0
# word_without_e = 0
# with open('words.txt', 'r') as words:
#   print("Words without e:")
#   for line in words:
#     total_words += 1
#     word = line.strip()
#     if has_no_e(word):
#       word_without_e += 1
#       print(word)

# print(f"Percentage of words without e: {round(word_without_e/total_words * 100, 2)}%")


# Exercise 9.3
def avoids(word, forbidden_letters):
  for l in word:
    if l in forbidden_letters:
      return False
  return True


forbidden_letters_input = str(input("Zadaj zakazane pismena: "))

word_num = 0
with open('words.txt', 'r') as words:
  for line in words:
    word = line.strip()
    if avoids(word, forbidden_letters_input):
      word_num += 1

print(word_num)

# Extra challenge part of exercise
english_abc = "abcdefghijklmnopqrstuvwxyz"

from itertools import combinations

# Load words to the memory
text_file_buffer = []
with open('words.txt', 'r') as words:
  for line in words:
    word = line.strip()
    text_file_buffer.append(word)

# Optimising english_abc
letters = {}

for w in text_file_buffer:
  for letter in w:
    if letter in letters:
      letters[letter] += 1
    else:
      letters[letter] = 1

letters = {k: v for k, v in sorted(letters.items(), key=lambda item: item[1], reverse=True)}
letters = [x[0] for x in list(letters.items())[:18]]
english_abc = ''.join([str(i) for i in english_abc if i not in letters])
print(f"Pouzite pismena: {english_abc}")


# Brute force search
total_number_of_words = len(text_file_buffer)
forbidden_letters = 5
least_excluding_combination = None
highest_percentage = None

for combination in combinations(english_abc, forbidden_letters):
  allowed_words_count = 0
  for word in text_file_buffer:
    if avoids(word, combination):
      allowed_words_count += 1
  percentage = allowed_words_count / total_number_of_words * 100
  if highest_percentage and least_excluding_combination:
    if percentage > highest_percentage:
      highest_percentage = percentage
      least_excluding_combination = combination
  else:
    least_excluding_combination = combination
    highest_percentage = percentage

print(f"Kombinacia pismen: {least_excluding_combination}, \nNevyradene slova: {highest_percentage : .3f}%")