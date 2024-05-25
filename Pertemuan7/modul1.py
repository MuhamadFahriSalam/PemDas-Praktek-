import modularitmatika

def main():
    a = int(input('Masukkan Nilai a: '))
    b = int(input('Masukkan Nilai b: '))
    c = float(b)
    
    print('a\t: %d' % a)
    print('b\t: %d'% b)
    print('c\t: %.2f\n' % c)
    
    print('a + b\t: %d' % modularitmatika.tambah(a, b))
    print('a - b\t: %d' % modularitmatika.kurang(a, b))
    print('a * b\t: %d' % modularitmatika.kali(a, b))
    print('a // b\t: %d' % modularitmatika.bagi(a, b))
    print('a / c\t: %d' % modularitmatika.bagi(a, c))
    print('a ** b\t: %d' % modularitmatika.pangkat(a, b))
    
if __name__ == '__main__':
    main()