# ------- Uloha 1 -------
def sucet(n):
  if n == 0:
    return n
  return n + sucet(n - 1)

# print(sucet(2))
# print(sucet(3))


# ------- Uloha 2 -------
def klav_sum(n):
  a = int(input("Zadaj cislo: "))
  if n == 1:
    return a
  return a + klav_sum(n - 1)

# print(klav_sum(3))


# ------- Uloha 3 -------
def pocet_parnych(n):
  a = int(input("Zadaj cislo: "))
  if n == 1:
    return 1 if a % 2 == 0 else 0
  if a % 2 == 0:
    return 1 + pocet_parnych(n - 1)
  else:
    return pocet_parnych(n - 1)

# print(pocet_parnych(4))


# ------- Uloha 4 -------
def najvacsie(n):
  a = int(input("Zadaj cislo: "))
  if n == 1:
    return a
  
  b = najvacsie(n - 1)
  return a if a > b else b


# print(najvacsie(3))


# ------- Uloha 5 -------
def je_sucet_parny(n):
  a = int(input("Zadaj cislo: "))
  if n == 1:
    return True if a % 2 == 0 else False

  parita_b = je_sucet_parny(n - 1)
  if not(a % 2 == 0 != parita_b):
    return True
  return False


# print(je_sucet_parny(3))


# ------- Uloha 6 -------
def test_prvociselnosti(a):
  if a < 2:
    raise ValueError("Prvocislo nemoze byt menise ako 2")
  for i in range(2, a):
    if a % i == 0:
      return False
  return True


def sucet_prvocisel(n):
  if n < 2:
    raise ValueError("Vstup musi byt vacsi ako 1")

  if n == 2:
    return 2
  
  if test_prvociselnosti(n):
    return n + sucet_prvocisel(n - 1)
  return sucet_prvocisel(n - 1)
  

# print(sucet_prvocisel(2))
# print(sucet_prvocisel(3))
# print(sucet_prvocisel(10))


# ------- Uloha 7 -------
# Watch video [x]
def premiestni(z, s, do):
  print(f"Premiestni disk z {z} do {s}")
  print(f"Premiestni disk z {s} do {do}")

def tower_of_hanoi(pocet_diskov, z, pomocne_miesto, do):
  if pocet_diskov == 0:
    return
  tower_of_hanoi(pocet_diskov - 1, z, do, pomocne_miesto)
  print(f"Premiestni disk z {z} do {do}")
  tower_of_hanoi(pocet_diskov - 1, pomocne_miesto, z, do)

# tower_of_hanoi(4, "A", "B", "C")


# ------- Uloha 8 -------
def is_palindrome(word):
  if len(word) == 0:
    return True
  if word[0] == word[-1]:
    return is_palindrome(word[1: -1])
  return False


# print(is_palindrome("noon"))
# print(is_palindrome("moon"))


# ------- Uloha 9 -------
def is_power(a, b):
  if a <= 0 or b <= 0:
    raise ValueError("a, b musia patrit do mnoziny N")
  if a < b and a != 1:
    return False
  if a // b == 0:
    return True
  if a % b == 0:
    return is_power(a / b, b)
  return False

# print(is_power(8, 2))
# print(is_power(9, 2))
# print(is_power(16, 4))
# print(is_power(32, 2))
# print(is_power(3, 4))


# ------- Uloha 10 -------
def gcd(a, b):
  if b == 0:
    return a
  return gcd(b, a % b)

# print(gcd(30, 20))
# prtin(gcd(8, 12))


# ------- Uloha 11 -------
import turtle

def koch(t, length):
  # Zadanie znie ze ked 
  # x < 3, ale v tom pripade 
  # strany vzoru budu 
  # kratke preto davam 15
  if length < 15:
    t.fd(length)
  else:
    koch(t, length / 3)
    t.lt(60)
    koch(t, length / 3)
    t.rt(120)
    koch(t, length / 3)
    t.lt(60)
    koch(t, length / 3)


def snowflake(t, length):
  for _ in range(3):
    koch(t, length)
    t.rt(120)
  
# ------------------------
bob = turtle.Turtle()

bob.speed(0)

bob.pu()
bob.setpos(-350, 200)
bob.pd()

# koch(bob, 700)
snowflake(bob, 700)

turtle.done()
# ------------------------