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
  najvacie = None
  while True:
    cislo = int(input("Zadaj cislo: "))
    if najvacie:
      if cislo > najvacie:
        najvacie = cislo
        poradie_najv = poradie
    else:
      najvacie = cislo
    if cislo == 0:
      return poradie_najv
    poradie += 1

# print(poradie_najvacsieho())


# -------- Uloha 5 --------