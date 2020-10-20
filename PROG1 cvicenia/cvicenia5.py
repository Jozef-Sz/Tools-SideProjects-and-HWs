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


# ------- Uloha 8 -------
def is_palindrome(word):
  if len(word) == 0:
    return True
  if word[0] == word[-1]:
    return is_palindrome(word[1: -1])
  return False


print(is_palindrome("noon"))
# print(is_palindrome("moon"))


# ------- Uloha 9 -------

