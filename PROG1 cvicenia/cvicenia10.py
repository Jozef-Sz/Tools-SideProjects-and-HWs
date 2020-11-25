# ---------- Uloha 1 ----------
def najcastejsie():
  zadane_cisla = []
  cislo = None
  najcastejsie = cislo
  while cislo != 0:
    cislo = int(input("Zadaj cislo: "))
    zadane_cisla.append(cislo)
    if zadane_cisla.count(cislo) > zadane_cisla.count(najcastejsie):
      najcastejsie = cislo
  return najcastejsie

print(najcastejsie())


# ---------- Uloha 2 ----------
# ------- Exercise 10.4 -------
# Write a function called chop that takes a list, modifies it 
# by removing the first and last elements, and returns None.
def chop(lst):
  lst.remove(lst[0])
  lst.pop()

# a = [1, 2, 3, 4]
# print(a)
# chop(a)
# print(a)


# ---------- Uloha 3 ----------
def matrix_add(a, b):
  if len(a) != len(b) or len(a[0]) != len(b[0]):
    raise ArithmeticError("Zadane matice nie je mozne scitat")
  matrix = [[0]*len(a[0]) for _ in range(len(a))]
  for i_row in range(len(a)):
    for i_col in range(len(a[0])):
      matrix[i_row][i_col] = a[i_row][i_col] + b[i_row][i_col] 
  return matrix

a_matrix = [
  [1, 1, 2],
  [3, 5, 8],
  [3, 1, 4]
]

b_matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

c_matrix = [
  [5, 2],
  [2, 4],
  [7, 8]
]

d_matrix = [
  [1, 2, 3],
  [5, 6, 7]
]

# print(matrix_add(a_matrix, b_matrix))
# print(matrix_add(a_matrix, c_matrix))


# ---------- Uloha 4 ----------
def matrix_mul(a, b):
  if len(a[0]) != len(b):
    raise ArithmeticError("Zadane matice nie je mozne vynasobit")
  matrix = [[0]*len(b[0]) for _ in range(len(a))]
  for i_row in range(len(matrix)):
    for i_col in range(len(matrix[0])):
      sum = 0
      for k in range(len(a[0])):
        sum += a[i_row][k] * b[k][i_col]
      matrix[i_row][i_col] = sum
  return matrix

# print(matrix_mul(a_matrix, b_matrix))


# ---------- Uloha 5 ----------
# Dva intervaly [a1, b1], [a2, b2] nemaju prienik vtedy a len vtedy,
# ak b1 < a2 alebo b2 < a1. 
def maju_spolocny_prienik(lst):
  if len(lst) < 2:
    raise ValueError("Min. 2 intervaly su potrebne na urcenie prieniku.")
  prienik = [lst[0][0], lst[0][1]]
  for i in range(1, len(lst)):
    if prienik[0] > lst[i][1] or prienik[1] < lst[i][0]:
      return False
    prienik[0] = max(prienik[0], lst[i][0])
    prienik[1] = min(prienik[1], lst[i][1])
  return True


a = [[1, 15], [8, 20]]  # True
b = [[0, 4], [5, 9]]  # False
c = [[1, 15], [5, 8], [6, 20]]  # True
d = [[1, 3], [5, 8], [10, 20]]  # False
e = [[1, 5], [4, 8], [6, 20]]   # False

# print(maju_spolocny_prienik(a))
# print(maju_spolocny_prienik(b))
# print(maju_spolocny_prienik(c))
# print(maju_spolocny_prienik(d))
# print(maju_spolocny_prienik(e))


# ---------- Uloha 6 ----------
# ------- Exercise 10.7 -------
# Write a function called has_duplicates that takes a list and returns True if there
# is any element that appears more than once. It should not modify the original list
def has_duplicates(lst):
  for elem in lst:
    if lst.count(elem) > 1:
      return True
  return False

# print(has_duplicates([1, 2, 3, 4, 5]))  # False
# print(has_duplicates([3, 5, 5, 12, 4])) # True


# ------- Exercise 10.8 -------
from random import randint, choice

def birthday_paradox(subjects, iterations=100):
  coincidence_count = 0
  for i in range(iterations):
    sample = [get_bday() for _ in range(subjects)]
    is_same_date = len(sample) != len(set(sample))
    if is_same_date:
      coincidence_count += 1
  return coincidence_count / iterations

def get_bday():
  day, month = None, randint(1, 12)
  if month in (1, 3, 5, 7, 8, 10, 12):
    day = randint(1, 31)
  elif month == 2:
    day = randint(1, choice([28, 28, 28, 29]))
  else:
    day = randint(1, 30)
  return (day, month)

pravdepodobnost = birthday_paradox(23, 10000)
print(f"Pravdepodobnost ludi s rovnakym datumom nar. {pravdepodobnost * 100}%")


# ------- Exercise 10.9 -------
import time

def versionone():
  lst = []
  with open("words.txt", "r") as txt:
    for line in txt:
      lst.append(0)

def versiontwo():
  lst = []
  with open("words.txt", "r") as txt:
    for line in txt:
      lst = lst + [0]

# t1 = time.perf_counter()
# versionone()
# t2 = time.perf_counter()
# versiontwo()
# t3 = time.perf_counter()
# print(f"Cas s append() {t2-t1}s. \nCas s t = t + [x] {t3-t2}s.")

# Conclusion: Append je omnoho rychlejsi ako t = t + [x] (Kebyze concatination upravime na t += [x]
# nebol by velky rozdiel, max par nanosekund). Dovod: Python interpreter je napisany v jazyku C. Teda
# pozname C, vieme si vysvetlit jednotlive aj na prvy pohlad nejednoznacne vlastnosti pythonu, ako aj tato.
# Zoznamy v pythone su v skutocnosti zoznamy v C-cku. Narozdiel od pythonu tieto zoznamy nie su dynamicke,
# maju vopred alokovanu pamat, kotru mozu vyuzit. Aby zoznamy pythonu boli dynamicke maju svoju kapacitu,
# co znamena ze maju niekolko miest vopred alokovanych i ked dany zoznam neobsahuje ziadny prvok. Kedze 
# append len zaplna vopred alokovane miesta a netreba po kazdy krat vytvarat novy zoznam, teda aj samotny
# procej je omnoho rychlejsi. Pri t = t + [x] po kazdy krat sa vytvori novy (redundantny) zoznam.


# ------- Exercise 10.10 -------
def in_bisect(lst, target):
  left, right = 0, len(lst)-1
  while left <= right:
    mid = (left + right) // 2
    if lst[mid] < target:
      left = mid + 1
    elif lst[mid] > target:
      right = mid - 1
    else:
      return True
  return False

# words = []
# with open("words.txt", "r") as txt:
#   for line in txt:
#     word = line.strip()
#     words.append(word)

# print(in_bisect(words, "believes"))  # True
# print(in_bisect(words, "Saitama"))   # False
# print(in_bisect(words, "proxy"))  # True
# print(in_bisect(words, "Puri-Puri Prisoner")) # False


# ------- Exercise 10.11 -------
def is_reversepair(a, b):
  return a == b[::-1]

# words = []
# with open("words.txt", "r") as txt:
#   for line in txt:
#     words.append(line.strip())
# 
# print("Vsetky reverse pair:")
# 
# # Wrong example
# # for i in range(len(words)):
# #   for j in range(i+1, len(words)):
# #     if is_reversepair(words[i], words[j]):
# #       print(f"  pair: {words[i]}, {words[j]}")
# 
# for word in words:
#   if in_bisect(words, word[::-1]):
#     print(f"  pair: {word}, {word[::-1]}")
# 
# # Malo by byt 885 takych parov vo words.txt


# ------- Exercise 10.12 -------
def is_interlock(words, il_word):
  return (in_bisect(words, il_word[::2]) and
          in_bisect(words, il_word[1::2]))

def is_triple_interlock(words, il_word):
  return (in_bisect(words, il_word[::3]) and
          in_bisect(words, il_word[1::3]) and
          in_bisect(words, il_word[2::3]))

# words = []
# with open("words.txt", "r") as txt:
#   for line in txt:
#     words.append(line.strip())
# 
# print("Kazdy interlock z words.txt:")
# for word in words:
#   if is_interlock(words, word):
#     print(f"  {word} je interlock {word[::2]} a {word[1::2]}")
#     
# print("Kazdy trojnasobny interlock:")
# for word in words:
#   if is_triple_interlock(words, word):
#     print(f"  {word} je interlock {word[::3]}, {word[1::3]} a {word[2::3]}")
