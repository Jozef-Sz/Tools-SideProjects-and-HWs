# -- Cast prva: rozcvicka --
# -------- Uloha 1 --------
def tretie_najvacsie_zadane(n):
  if n == 1:
    return int(input("Zadaj cislo: "))

  tretie_najvacsie = None
  druhe_najvacsie = None
  najvacsie = None

  for _ in range(n):
    cislo = int(input("Zadaj cislo: "))
    if najvacsie:
      if najvacsie < cislo:
        tretie_najvacsie = druhe_najvacsie
        druhe_najvacsie = najvacsie
        najvacsie = cislo
      else:
        if druhe_najvacsie:
          if druhe_najvacsie < cislo:
            tretie_najvacsie = druhe_najvacsie
            druhe_najvacsie = cislo
          else:
            if tretie_najvacsie:
              if tretie_najvacsie < cislo:
                tretie_najvacsie = cislo
            else:
              tretie_najvacsie = cislo
        else:
          druhe_najvacsie = cislo
    else:
      najvacsie = cislo
  return tretie_najvacsie


# # Cheat verzia
# def tretie_najvacsie_zadane(n):
#   cisla = []
#   for _ in range(n):
#     cislo = int(input("Zadaj cislo: "))
#     cisla.append(cislo)
#   cisla.sort()
#   return cisla[n - 3]


# print(tretie_najvacsie_zadane(4))


# -- Cast druha: priklady --
# -------- Uloha 1 --------
def suma_kladnych():
  sum = 0
  cislo = int(input("Zadaj cislo: "))
  while cislo > 0:
    sum += cislo
    cislo = int(input("Zadaj cislo: "))
  return sum

# print(suma_kladnych())


# -------- Uloha 2 --------
def stvorce_do(n):
  if n < 0:
    return None
  counter = 0
  while counter ** 2 < n:
    print(counter ** 2)
    counter += 1

# stvorce_do(10)


# -------- Uloha 3 --------
def pow(base, exp):
  result = base
  counter = exp
  while counter > 1:
    result *= base
    counter -= 1
  return result

# Feel free to just import pow from math, but 
# probably the function above is expected XD
# from math import pow


def najvacsie_x(n):
  if n < 0:
    return None
  x = 0
  while pow(2, x) < n and pow(2, x + 1) < n:
    x += 1
  return x

# print(najvacsie_x(10))


# -------- Uloha 4 --------
def poradie_najvacsieho():
  poradie = 1
  poradie_najv = 1
  najvacsie = int(input("Zadaj cislo: "))
  while True:
    cislo = int(input("Zadaj cislo: "))
    poradie += 1
    if cislo > najvacsie:
      najvacsie = cislo
      poradie_najv = poradie
    if cislo == 0:
      return poradie_najv

# print(poradie_najvacsieho())


# -------- Uloha 5 --------
def pocet_vacsich():
  pocet = 0
  predosle = int(input("Zadaj cislo: "))
  while True:
    cislo = int(input("Zadaj cislo: "))
    if cislo > predosle:
      pocet += 1
    if cislo == 0:
      return pocet
    predosle = cislo

# print(pocet_vacsich())


# -------- Uloha 6 --------
def pocet_rovnych_najv():
  najvacsie = int(input("Zadaj cislo: "))
  pocet_rov = 0
  while True:
    cislo = int(input("Zadaj cislo: "))
    if cislo > najvacsie:
      najvacsie = cislo
      pocet_rov = 0
    if cislo == najvacsie:
      pocet_rov += 1
    if cislo == 0:
      return pocet_rov

# print(pocet_rovnych_najv())


# -------- Uloha 7 --------
def dlzka_podpostupnosti():
  dlzka = 1
  cislo = None
  najdlhsia_dlzka = 1
  predosle_cislo = int(input("Zadaj cislo: "))
  while cislo != 0:
    cislo = int(input("Zadaj cislo: "))
    if cislo == predosle_cislo:
      dlzka += 1
    else:
      if dlzka > najdlhsia_dlzka:
        najdlhsia_dlzka = dlzka
        dlzka = 1
    predosle_cislo = cislo
  return najdlhsia_dlzka

# print(dlzka_podpostupnosti())


# -------- Uloha 8 --------
cache = {}

def fibonacci(n):
  if n in cache:
    return cache[n]
  if n == 0:
    value = 0
  elif n == 1:
    value = 1
  else:
    value = fibonacci(n - 1) + fibonacci(n - 2)
  cache[n] = value
  return value


# Brute Force Method
def fibonacci_index(x):
  index = 0
  while True:
    fib_cislo = fibonacci(index)
    if fib_cislo == x:
      return index
    elif fib_cislo < x:
      index += 1
    else:
      return -1

from math import sqrt, log

# Mathematical Method
def fibonacci_index_b(x):
  a = 5 * x**2 + 4
  b = 5 * x**2 - 4
  a_sr = int(sqrt(a))
  b_sr = int(sqrt(b))
  if (a_sr * a_sr == a) or (b_sr * b_sr == b):
    fib_index = 2.078087 * log(x) + 1.672276
    return round(fib_index)
  else:
    return -1

# print(fibonacci_index(4))
# print(fibonacci_index(8))
# print(fibonacci_index(2))
# print(fibonacci_index(9))


# -------- Uloha 9 --------
# from math import sqrt
def mysqrt(a):
  pass


def test_square_root(range):
  