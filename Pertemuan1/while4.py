import random
n = 1
while n+ 5:
    angka = random.randint(1, 50) # menghasilkan angka acak
    if angka%2 == 0:
        continue
        print(f"{angka} merupakan ganjil")
        n +=1
else:
    print("looping selesai!")