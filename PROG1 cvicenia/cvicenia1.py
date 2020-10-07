import turtle as t

##### Moje funkcie #####
def nUholnik(n, strana):
    for i in range(n):
        t.forward(strana)
        t.left(360 / n)

def odmocnina(n):
    pass


##### 1. Vykreslite štvorec #####
# for i in range(4):
#    t.forward(100)
#    t.left(90)


##### 2. Vykreslite rovnoramenný trojuholník #####
# for i in range(3):
#     t.forward(100)
#     t.left(360/3)


##### 3. Vykreslite rovnostranný päťuholník #####
# for i in range(5):
#     t.forward(100)
#     t.left(360/5)


##### 4.Vykreslite Obrázok 1 zo súboru (Obrázok 1) #####
# for i in range(4):
#     t.forward(30)
#     t.left(90)
#     t.forward(30)
#     t.left(90)

#     t.forward(30)
#     t.right(90)


##### 4.Vykreslite Obrázok 1 zo súboru (Obrázok 2) #####
# for i in range(2):
#     for j in range(6):
#         t.forward(30)
#         t.left(90)
#         t.forward(30)
#         t.right(90)

#     t.left(180)

#     for j in range(5):
#         t.forward(30)
#         t.right(90)
#         t.forward(30)
#         t.left(90)


##### 4.Vykreslite Obrázok 1 zo súboru (Obrázok 3) #####
# for i in range(10):
#     nUholnik(5, 90)
#     t.left(360/10)


##### 4.Vykreslite Obrázok 1 zo súboru (Obrázok 4) #####
# for i in range(12):
#     nUholnik(12, 90)
#     t.left(360/12)


##### 4.Vykreslite Obrázok 1 zo súboru (Obrázok 5) #####

t.done()