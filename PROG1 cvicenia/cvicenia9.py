# ---------- Uloha 1 ----------
# Exercise 10.1
def nested_sum(n_list):
  sum = 0
  for element in n_list:
    for num in element:
      sum += num
  return sum

# print(nested_sum([[1, 2], [3], [4, 5, 6]]))

# Exercise 10.2
def cumsum(lst):
  new_lst = []
  for i in range(len(lst)):
    new_lst.append(sum(lst[:i+1]))
  return new_lst

# print(cumsum([1, 2, 3])) # [1, 3, 6]

# Exercise 10.3
def middle(lst):
  return lst[1:len(lst)-1]

# def middle(lst):
#   return [n for i, n in enumerate(lst) if (i != 0) and (i != len(lst)-1) ]

# a = [1, 2, 3, 4, 12]
# print(a)
# print(middle(a))
# print(a)

# ---------- Uloha 2 ----------
# Exercise 10.5
def is_sorted(a):
  return a == sorted(a)

# print(is_sorted([1, 2, 3]))
# print(is_sorted([1, 44, 3]))
# print(is_sorted(['a', 'b', 'c']))
# print(is_sorted(['a', 'd', 'c']))


# ----------- Uloha 3 ----------
# def sum_even_index(lst):
#   sum = 0
#   for n in lst[::2]:
#     sum += n
#   return sum

def sum_even_index(lst):
  evens = [n for i, n in enumerate(lst) if i % 2 == 0]
  return sum(evens)

# print(sum_even_index([3, 6, 4, 6, 2]))
# print(sum_even_index([1, 6, 1, 6, 1]))


# ---------- Uloha 4 ----------
def ulohastyri(lst):
  pocet = 0
  index = 1
  while index < len(lst) - 1:
    if (lst[index] > lst[index -1]) and (lst[index] > lst[index + 1]):
      pocet += 1
    index += 1
  return pocet

# print(ulohastyri([1, 5, 2, 12, 8, 9]))


# ---------- Uloha 5 ----------
def pocet_roznych_prvkov(lst):
  return len(set(lst))
  
# print(pocet_roznych_prvkov([1, 2, 2, 4, 5, 4]))    # 4
# print(pocet_roznych_prvkov([5, 5]))                # 1
# print(pocet_roznych_prvkov([5, 5, 1, 12, 12, 12])) # 3


# ---------- Uloha 6 ----------
def unique_items_count(lst):
  work_lst = lst.copy()
  lst_set = set(lst)
  for elm in lst_set:
    work_lst.remove(elm)
  unique_elements = list(filter(lambda x: x not in work_lst, lst))
  return len(unique_elements)

def unique_items_count2(lst):
  pocet = 0
  for elm in lst:
    if lst.count(elm) == 1:
      pocet += 1
  return pocet

# arr = [1, 2, 2, 3, 15, 15]
# print(unique_items_count2(arr))


# ---------- Uloha 7 ----------
# Exercise 10.6
def is_anagram(a_word, b_word):
  if sorted(list(a_word)) == sorted(list(b_word)):
    return True
  return False
  

print(is_anagram("elet", "etel")) # True
print(is_anagram("forty five", "over fifty")) # True
print(is_anagram("satu", "utas")) # True
print(is_anagram("abcd", "efgh")) # False
print(is_anagram("coca", "cola")) # False
