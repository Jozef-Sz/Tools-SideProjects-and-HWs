import turtle

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
  elif a == b:
    return 2
  elif b == c:
    return 2
  elif a == c:
    return 2
  else:
    return 0

# print(pocet_rovnakych(4, 4, 4))
# print(pocet_rovnakych(1, 5, 7))
# print(pocet_rovnakych(3, 3, 5))
# print(pocet_rovnakych(6, 5, 6))
# print(pocet_rovnakych(3, 5, 5))


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
  cisla = []
  for i in range(n):
    cislo = int(input("Zadaj cislo: "))
    cisla.append(cislo)
  cisla.sort()
  return cisla[n - 2]

# print(druhe_najvacsie_zadane(5))


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
# Maybe later I'll finish