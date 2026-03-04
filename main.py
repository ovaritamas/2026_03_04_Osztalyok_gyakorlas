from auto import Auto
import random as r


auto1 = Auto("Toyota", "Corolla", 2006)
auto2 = Auto("Nissan", "Note", 2015)
auto3 = Auto("Ford", "Focus", 2005)
auto4 = Auto("Volkswagen", "Passat", 2004)
auto5 = Auto("Opel", "Astra", 2007)

autok = [auto1, auto2, auto3, auto4, auto5]
for auto in autok:
    print(auto)

for auto in autok:
    auto.gyorsit(r.randint(10, 170))  
    print(auto)

year = 2026
autok_szama = len(autok)
ossz_eletkor = 0
for auto in autok:
    kor = year - auto.gyartasi_ev
    ossz_eletkor += kor

atlag_eletkor = ossz_eletkor / autok_szama
print(f"Az autók átlag életkora: {atlag_eletkor} év")

legoregebb = autok[0]
for auto in autok:
    if auto.gyartasi_ev < legoregebb.gyartasi_ev:
        legoregebb = auto

legoregebb_eletkor = year - legoregebb.gyartasi_ev

print(f"A legöregebb autó: {legoregebb.marka} {legoregebb.tipus} {legoregebb.gyartasi_ev}, életkora:  {legoregebb_eletkor}")


#print(auto1)
#print(auto2)

#auto1.gyorsit(150)
#print(auto1)