# TUGAS 1
def main():
    a = 13
    b = 45.67
    
    print('sebelum diubah:')
    print('Nilai a\t\t:', a)
    print('Nilai a\t\t:', b)
    print('Tipe data a\t:', type(a))
    print('Tipe data a\t:', type(b))
    print('Identitas a\t:', id(a))
    print('Identitas a\t:', id(b))
    
    a = 'python'
    b = True
    
    print('sebelum diubah:')
    print('Nilai a\t\t:', a)
    print('Nilai a\t\t:', b)
    print('Tipe data a\t:', type(a))
    print('Tipe data a\t:', type(b))
    print('Identitas a\t:', id(a))
    print('Identitas a\t:', id(b))
    
if __name__ == '__main__':
    main()
    
    
# TUGAS 2
def main():
    bahasa = 'pyhon'
    versi = 3
    
    print(bahasa, versi) 
    print(bahasa + ' ' + str(versi))
    print('%s %d' % (bahasa, versi))
    print('{} {}' .format(bahasa, versi))
    print('{0} {1}'.format(bahasa, versi))
    
if __name__== '__main__':
    main()


# TUGAS 3
def main():
    alas = 4.0
    tinggi = 5.0
    luas = alas * tinggi / 2
    
    print('Menghitung luas segitiga')
    print(f'Alas\t: {alas}')
    print(f'Tinggi\t: {tinggi}')
    print(f'Luas/t: {luas}')
    
if __name__ == '__main__' :
    main()



# TUGAS 4
def main():
    print('Masukkan data diri Anda')
    nama = input('Nama\t: ')
    alamat = input('Alamat\t: ')
    telephone = input('No telephone\t: ')
    
    print('\nData diri: %s, %s, %s, %' (nama, alamat, telephone))
    
    print('\ntype(nama\t: %s)' % type(nama))
    print('\ntype(alamat\t: %s)' % type(alamat))
    print('\ntype(telephone\t: %s)' % type(telephone))
   
if __name__ == '__main__' :
    main()
 
 
 
#  TUGAS 5
def main():
    print('Menghitung luas persegi panjang')
    panjang = int(input('Panjang\t: '))
    lebar = int(input('Lebar\t: '))
    
    luas = panjang * lebar
    
    print('\nluas = %d' % luas)
    
if __name__ == '__main__' :
    main()



# TUGAS 6
import math 

def main():
    print('Menghitung luas lingkaran')
    radius = float(input('Jari-jari\t: '))
    
    luas = math.pi * (radius ** 2)
    
    print('\nLuas = %.2f' % luas)
    
if __name__ == '__main__' :
    main()
