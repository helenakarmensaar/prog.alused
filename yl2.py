# yl2
# Kirjuta programm, mis küsib kasutajalt raadiuse ja arvutab ringi pindala ja ümbermõõdu. (math.pi)

# 1) Küsime kasutajalt raadiuse
# 2) Arvutame ringi pindala
# 3) Arvutame ringi raadiuse
# 4) Väljastame C, S

from math import pi

radius = float(input("Sisesta raadius: "))

area = pi * radius ** 2
print("Pindala:", area)

perimeter = 2 * pi * radius 
print("Ümbermõõt:", perimeter)