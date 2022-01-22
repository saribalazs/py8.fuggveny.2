'''
2. Feladat
Írj egy programot, amely tartalmaz egy 'paros_e' nevű függvényt, amely True értékkel tér vissza, ha a paraméterként átvett listaelemek (egész számok) között van páros, ellenkező esetben a visszatérési érték False! 
A program tartalmazza a függvény hívását is!
'''
def paros_e(n , *args):
    num = n
    for i in args:
        if i % 2 == 0:
            return True
        else:
            return False



print(paros_e(1485411541148461,221545485484))