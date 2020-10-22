# ----- Uloha 1 -----
def numbers_to():
  n = int(input("Cisla od 1 po: "))
  for i in range(1, n+1):
    print(i)

# numbers_to()


# ----- Uloha 2 -----
def test_parity(n):
  return n % 2 == 0

# print(test_parity(11))
# print(test_parity(4542))


# ----- Uloha 3 -----
def minimum_dvoch(a, b):
  if a < b:
    return a
  else:
    return b

# print(minimum_dvoch(4, 100))


# ----- Uloha 4 -----
def minimum_troch(a, b, c):
  if a < b:
    return minimum_dvoch(a, c)
  else:
    return minimum_dvoch(b, c)

# print(minimum_troch(1, 5, 9))
# print(minimum_troch(10, 5, 30))
# print(minimum_troch(190, 54, 2))


# ----- Uloha 5 -----
import turtle

def polygon(n, len):
  for _ in range(n):
    turtle.fd(len)
    turtle.lt(360 / n)
  turtle.done()

def menu():
  sign = str(input("Zadaj znak z klavesnice: "))
  if sign == "s":
    polygon(4, 50)
  elif sign == "t":
    polygon(3, 50)
  else:
    print("Zadali ste neplatny vstup!")

# menu()


# ----- Uloha 6 -----
def pocet_rovnakych(a, b, c):
  if a == b and b == c:
    return 3
  elif a == b or b == c or a == c:
    return 2
  else:
    return 0

print(pocet_rovnakych(4, 4, 4))
print(pocet_rovnakych(1, 5, 7))
print(pocet_rovnakych(3, 3, 5))
print(pocet_rovnakych(6, 5, 6))
print(pocet_rovnakych(3, 5, 5))


# ----- Uloha 7 -----
def delitelne_piatimi(n):
  pocet_cisel = 0
  for i in range(n):
    cislo = int(input("Zadaj cislo: "))
    if cislo % 5 == 0:
      pocet_cisel += 1
  print(f"Pocet cisel zo zadanych cisel, ktore su delitelne 5 je: {pocet_cisel}")

# delitelne_piatimi(4)


# ----- Uloha 8 -----
def suma(n):
  suma = 0
  for i in range(n):
    cislo = int(input("Zadaj cislo: "))
    suma += cislo
  print(f"Sucet vsetkych cisel, ktore si zadal je {suma}")

# suma(5)


# ----- Uloha 9 -----
def minimum_zadane(n):
  najmensie_cislo = None
  for i in range(n):
    cislo = int(input("Zadaj cislo: "))
    if najmensie_cislo:
      if cislo < najmensie_cislo:
        najmensie_cislo = cislo
    else:
      najmensie_cislo = cislo
  return najmensie_cislo

# print(minimum_zadane(4))


# ----- Uloha 10 -----
def druhe_najvacsie_zadane(n):
  if n == 1:
    return int(input("Zadaj cislo: "))

  druhe_najvacsie = None
  najvacsie = None

  for i in range(n):
    cislo = int(input("Zadaj cislo: "))
    if najvacsie:
      if cislo > najvacsie:
        druhe_najvacsie = najvacsie
        najvacsie = cislo
    else:
      najvacsie = cislo
  return druhe_najvacsie 


# # Cheat verzia
# def druhe_najvacsie_zadane(n):
#   cisla = []
#   for i in range(n):
#     cislo = int(input("Zadaj cislo: "))
#     cisla.append(cislo)
#   cisla.sort()
#   return cisla[n - 2]

print(druhe_najvacsie_zadane(5))


# ----- Uloha 11 -----
def delitenost(a, d):
  return a % d == 0

# print("Delitele cisla 12 su:")
# for i in range(1, 13):
#   if delitenost(12, i):
#     print(i)


# ----- Uloha 12 -----
def test_prvociselnosti(a):
  if a < 2:
    raise ValueError("Prvocislo nemoze byt menise ako 2")
  for i in range(2, a):
    if delitenost(a, i):
      return False
  return True

# print("Vsetky provocisla z mnoziny (2, 50) su:")
# for i in range(3, 50):
#   if test_prvociselnosti(i):
#     print(i)


# ----- Uloha 13 -----
# print("Vsetky provocisla mensie ako 50 su:")
# for i in range(2, 50):
#   if test_prvociselnosti(i):
#     print(i)


# ----- Uloha 14 -----
def pohyb_veze(x1, y1, x2, y2):
  if (((x1 < 1) or (x1 > 8)) or ((y1 < 1) or ( y1 > 8)) or 
      ((x2 < 1) or (x2 > 8)) or ((y2 < 1) or ( y2 > 8))):
    raise ValueError("parametre musia nadobudat hodnotu z monoziny <1, 8>")  
  
  if x1 == x2 or y1 == y2:
    return True
  
  return False


# print(pohyb_veze(4, 4, 5, 5))
# print(pohyb_veze(4, 4, 5, 4))
# print(pohyb_veze(4, 4, 5, 3))
# print(pohyb_veze(4, 4, 4, 5))
# print(pohyb_veze(4, 4, 3, 5))
# print(pohyb_veze(4, 4, 4, 3))
# print(pohyb_veze(4, 4, 3, 4))


# ----- Uloha 15 -----
def is_black(x, y):
  if x % 2 == 0 and y % 2 == 0:
    return True
  elif x % 2 != 0 and y % 2 != 0:
    return True
  else:
    return False


def rovnaka_farba(x1, y1, x2, y2):
  if (((x1 < 1) or (x1 > 8)) or ((y1 < 1) or ( y1 > 8)) or 
      ((x2 < 1) or (x2 > 8)) or ((y2 < 1) or ( y2 > 8))):
    raise ValueError("parametre musia nadobudat hodnotu z monoziny <1, 8>")
  
  if not(is_black(x1, y1) != is_black(x2, y2)):
    return True
  return False


# print(rovnaka_farba(1, 1, 2, 6))
# print(rovnaka_farba(2, 2, 2, 5))
# print(rovnaka_farba(2, 2, 2, 4))
# print(rovnaka_farba(2, 3, 3, 2))
# print(rovnaka_farba(2, 3, 7, 8))
# print(rovnaka_farba(2, 3, 8, 8))
# print(rovnaka_farba(5, 7, 5, 7))
# print(rovnaka_farba(2, 6, 3, 1))


# ----- Uloha 16 -----
from math import sqrt

def pohyb_krala(x1, y1, x2, y2):
  if (((x1 < 1) or (x1 > 8)) or ((y1 < 1) or ( y1 > 8)) or 
      ((x2 < 1) or (x2 > 8)) or ((y2 < 1) or ( y2 > 8))):
    raise ValueError("parametre musia nadobudat hodnotu z monoziny <1, 8>")

  vzdialenost = sqrt((x1 - x2)**2 + (y1 - y2)**2)
  if vzdialenost <= sqrt(2):
    return True
  return False


# print(pohyb_krala(8, 1, 1, 1))
# print(pohyb_krala(8, 1, 1, 8))
# print(pohyb_krala(8, 1, 8, 8))
# print(pohyb_krala(1, 1, 1, 2))
# print(pohyb_krala(1, 1, 2, 2))
# print(pohyb_krala(1, 1, 2, 1))
# print(pohyb_krala(4, 4, 6, 6))
# print(pohyb_krala(4, 4, 2, 2))


# ----- Uloha 17 -----
def pohyb_strelca(x1, y1, x2, y2):
  if (((x1 < 1) or (x1 > 8)) or ((y1 < 1) or ( y1 > 8)) or 
      ((x2 < 1) or (x2 > 8)) or ((y2 < 1) or ( y2 > 8))):
    raise ValueError("parametre musia nadobudat hodnotu z monoziny <1, 8>")
  
  if abs(x1 - x2) == abs(y1 - y2):
    return True
  return False


# print(pohyb_strelca(4, 4, 5, 5))
# print(pohyb_strelca(4, 4, 5, 4))
# print(pohyb_strelca(4, 4, 5, 3))
# print(pohyb_strelca(4, 4, 4, 5))
# print(pohyb_strelca(4, 4, 3, 5))
# print(pohyb_strelca(4, 4, 4, 3))
# print(pohyb_strelca(4, 4, 3, 4))


# ----- Uloha 18 -----
def pohyb_damy(x1, y1, x2, y2):
  if (((x1 < 1) or (x1 > 8)) or ((y1 < 1) or ( y1 > 8)) or 
      ((x2 < 1) or (x2 > 8)) or ((y2 < 1) or ( y2 > 8))):
    raise ValueError("parametre musia nadobudat hodnotu z monoziny <1, 8>")
  if pohyb_veze(x1, y1, x2, y2) or pohyb_strelca(x1, y1, x2, y2):
    return True
  return False


# print(pohyb_damy(1, 1, 2, 2))
# print(pohyb_damy(1, 1, 2, 3))
# print(pohyb_damy(5, 6, 3, 3))
# print(pohyb_damy(3, 3, 1, 1))
# print(pohyb_damy(6, 5, 2, 5))


# ----- Uloha 19 -----
def pohyb_jazdca(x1, y1, x2, y2):
  if (((x1 < 1) or (x1 > 8)) or ((y1 < 1) or ( y1 > 8)) or 
      ((x2 < 1) or (x2 > 8)) or ((y2 < 1) or ( y2 > 8))):
    raise ValueError("parametre musia nadobudat hodnotu z monoziny <1, 8>")

  if abs((x1 - x2) * (y1 - y2)) == 2:
    return True
  return False


# print(pohyb_jazdca(1, 1, 1, 4))
# print(pohyb_jazdca(1, 1, 8, 8))
# print(pohyb_jazdca(2, 4, 3, 2))
# print(pohyb_jazdca(5, 2, 4, 4))
# print(pohyb_jazdca(2, 8, 3, 7))
