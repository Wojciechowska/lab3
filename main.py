import random
import math
#zad1
# a = [1-x for x in range(1, 11)]
# print(a)
# b = [4 ** i for i in range(8)]
# print(b)
# c = [x for x in b if x % 2 == 0]
# print(c)

#zad2
# listy1 = []
# for i in range(10):
#     listy1.append(random.randint(0, 1000))
# listy2 = [x for x in listy1 if x % 2 == 0]
# print(listy1)
# print(listy2)

# #zad3
# produkty = {'jajka':'sztuki', 'mięso':'kg',  'mleko':'litry', 'jabłko':'sztuki', 'chleb':'sztuki'}
# lista_produktow = [x for x, y in produkty.items() if y == 'sztuki']
# print(lista_produktow)

# #zad4
# def czy_prostokatny(a, b, c):
#     if (a**2 + b**2 == c**2):
#         print("Trójkąt jest prostokątny")
#     else:
#         print("Trójkąt nie jest prostokątny")
#
# print(czy_prostokatny(3, 4, 5))
# print(czy_prostokatny(3, 4, 7))

# #zad5
# def pole_trapezu(a = 0, b = 0, h = 0):
#     if (a <= 0 or b <=0 or h <= 0):
#         return 'Pole trapezu nie istnieje'
#     else:
#         return (a + b) * h / 2
#
# print(pole_trapezu(2, 4, 5))
# print(pole_trapezu(10, 2))
# print(pole_trapezu(a = 2, h = 5, b = 1))

# #zad6
# def iloczyn_ciagu(a=1, b=4, ile=10):
#     iloczyn = 1
#     for i in range(ile):
#         iloczyn *= a
#         a *= b
#     return iloczyn
# print(iloczyn_ciagu(2, 3, 3))

#zad7 (chyba nie o to chodziło)
# def iloczyn_ciagu(*, a=1, b=4, ile=10):
#     iloczyn = 1
#     for i in range(ile):
#         iloczyn *= a
#         a *= b
#     return iloczyn
# print(iloczyn_ciagu(ile = 4))

#zad8
# def lista_zakupow(**zakupy):
#     ilosc = len(zakupy)
#     wartosc = sum([cena for cena in zakupy.values()])
#     return ilosc, wartosc
#
# zakupy = {'chleb':10, 'mleko':5, 'jajka':12}
# ilosc, wartosc = lista_zakupow(**zakupy)
# print(f'Liczba produktów: {ilosc}')
# print(f'Wartość zakupów: {wartosc} zł')

#zad9
# print('Podaj liczbę do spierwiastkowania:')
# a = float(input())
# try:
#     wynik = math.sqrt(a)
#     print(f"Pierwiastek z {a} to {wynik:.2f}")
# except ValueError:
#     print('Podana liczba jest liczbą ujemną')

