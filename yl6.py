# yl6
# Kirjuta programm, mis leiab kolmest kasutaja poolt sisestatud arvust maksimumi (ära kasuta max funktsiooni). 
# (loogikatehted - logic operators)

# 1) Küsime kasutajalt arvu 1
# 2) Küsime kasutajalt arvu 2
# 3) Küsime kasutajalt arvu 3
# 4) Leia maksimum
# 5) Väljasta see

a = int(input("Sisesta esimene täisarv: "))
b = int(input("Sisesta teine täisarv: "))
c = int(input ("Sisesta kolmas täisarv: "))

if a > b and a > c:
    print("Maksimum on", a)

elif b > c:
    print("Maksimum on", b)

else:
    print("Maksimum on", c)