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
  for i, n in enumerate(lst):
    p_sum = 0
    for j in range(i + 1):
      p_sum += lst[j]
    new_lst.append(p_sum)
  return new_lst

# print(cumsum([1, 2, 3]))

# Exercise 10.3
def middle(lst):
  return lst[1:len(lst)-1]

# print(middle([1, 2, 3, 4]))


# ---------- Uloha 2 ----------
# Exercise 10.5
def is_sorted(a):
  return a == sorted(a)

# print(is_sorted([1, 2, 3]))
# print(is_sorted([1, 44, 3]))
# print(is_sorted(['a', 'b', 'c']))
# print(is_sorted(['a', 'd', 'c']))


# ----------- Uloha 3 ----------
def sum_even_index(lst):
  sum = 0
  for n in lst[::2]:
    sum += n
  return sum

# print(sum_even_index([3, 6, 4, 6, 2]))


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
# print(ulohastyri([1, 5, 6, 12, 8, 9]))


# ---------- Uloha 5 ----------

