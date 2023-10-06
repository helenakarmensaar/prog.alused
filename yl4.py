# yl4
# Kirjuta programm, mis leiab kahest kasutaja poolt sisestatud arvust miinimumi 
# (ära kasuta min funktsiooni). (muutuja - variable, tingimus - condition, if-lause - if statement)

# 1) Küsime kasutajalt arv 1
# 2) Küsi kasutajalt arv 2
# 3) Leia miinimum
# 4) Väljasta see

a = input("Sisesta esimene täisarv: ")
b = input("Sisesta teine täisarv: ")
if int(b) > int(a):
    print("Miinimum on", a)
else:
    print("Miinimum on", b)
