# Uloha 1A a 1B
def tretia_mocnina(a):
    return a**3

# tretia_mocnina(5)


# Uloha 2A a 2B
def priemer_troch(a, b, c):
    return (a + b + c) / 3

# priemer_troch(5, 6, 7)


# Uloha 3
def fn(n):
    for i in range(1, n + 1):
        print(i)

# fn(5)


# Uloha 4
def fn1(n):
    for i in range(100, 100 + n):
        print(i)

# fn1(3)


# Uloha 5
def fn2(n):
    for i in range(2, (n+1) * 2, 2):
        print(i)

# fn2(4)


# Uloha 6
def fn3(n):
    for i in range(n, 0, -1):
        print(i)

# fn3(5)


# Uloha 7
def fn4(n):
    sum = 0
    for i in range(1, n+1):
        sum += i**2
    
    return sum

# print(fn4(3))


# Uloha 8
def draw_grid(n):
    side_len = 4
    
    for x in range(n):
        buffer = ''
        for i in range(n):
            buffer += '+'
            for j in range(side_len):
                buffer += '-'
        buffer += '+'
        print(buffer)
        buffer = ''
        for i in range(n):
            buffer += '|'
            for j in range(side_len):
                buffer += ' '
        buffer += '|'

        print(buffer)

    buffer = ''
    for i in range(n):
        buffer += '+'
        for j in range(side_len):
            buffer += '-'
    buffer += '+'
    print(buffer)

# draw_grid(2)
# draw_grid(3)
# draw_grid(5)


# Uloha 8 (Refactored)
def draw_grid_r(n):
    cell_size = 4
    line = ''

    for i in range(n):
        line += '+'
        line += cell_size * '-'
    line += '+'

    for sides in range(n):
        print(line)

        for i in range(n):
            print('|', end='')
            print(cell_size * ' ', end='')
        print('|')

    print(line)

draw_grid_r(2)
draw_grid_r(3)
draw_grid_r(5)


# Uloha 9
def aritmeticka_postupnost(a, d, N):
    print(a)
    prev = a
    for i in range(N):
        prev += d
        print(prev)

# aritmeticka_postupnost(0, 3, 5)


# Uloha 10
def geo_postupnost(a, r, N):
    print(a)
    prev = a
    for i in range(N):
        prev *= r
        print(prev)

# geo_postupnost(1, 2, 5)


# Uloha 11
def geo_rad(a, r, N):
    prev = a
    sum = a
    print(sum)
    for i in range(N):
        prev *= r
        sum += prev
        print(sum)

# geo_rad(1, 2, 5)


# Uloha 12
def geo_rad_abs(a, r, N):
    prev = a
    sum = a
    print(sum)
    for i in range(N):
        prev *= abs(r)
        sum += prev
        print(sum)

a = 1
r = 0.5
N = 10

print('Target number:', 1/(1 - abs(r)))
geo_rad_abs(a, r, N)