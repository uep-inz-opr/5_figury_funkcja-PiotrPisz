from cmath import sqrt
import math
def oblicz_pole(a):
    if len(a)==1:
        wynik = math.pi*a[0]*a[0]
        wynik=round(wynik,2)
    elif len(a)==2:
        wynik = a[0]*a[1]
        wynik=round(wynik,2)
    elif len(a)==3:
        s = (a[0] + a[1] + a[2])/2
        wynik = math.sqrt(s*(s - a[0]) * (s - a[1]) * (s - a[2]))
        wynik = round(wynik, 2)
    else:
        return "Błąd: można podać maksymalnie 3 liczby"
    return wynik

pole=0
ile_figur = input()
ile_figur = int(ile_figur)
for i in range(ile_figur):
    figura = input().strip()
    figura = figura.split()
    for j in range(len(figura)):
        figura[j]=float(figura[j])

    wynik_funkcji = oblicz_pole(figura)
    if type(wynik_funkcji) is not float:
        pole="Błąd: można podać maksymalnie 3 liczby"
        break
    pole = pole + wynik_funkcji
    pole = round(pole, 2)
print(pole)