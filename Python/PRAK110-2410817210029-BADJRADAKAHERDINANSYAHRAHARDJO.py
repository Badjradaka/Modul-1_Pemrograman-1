import math
alas = 5
tinggi = 12
miring = math.sqrt(alas**2 + tinggi**2)
keliling = (alas + tinggi + miring)
luas = ((alas * tinggi) / 2)
print("Diketahui :")
print("Alas = %d cm" % (alas))
print("Tinggi = %d cm" % (tinggi))
print()
print("Jawab :")
print("Sisi A = %d cm" % (tinggi))
print("Sisi B = %d cm" % (miring))
print("Sisi C = %d cm" % (alas))
print("Keliling = %d cm" % (keliling))
print("Luas = %d cm" % (luas))
