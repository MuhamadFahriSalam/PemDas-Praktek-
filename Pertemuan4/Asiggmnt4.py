import sys

def main():
    a = float(input('Masukkan nilai a: '))
    b = float(input('Masukkan nilai b: '))
    
    if b == 0:
        print('Salah: nilai b tidak boleh nol.')
        sys.exit(1)
        
    c = a / b
    print('\n%2f /%.2f = %.2f' % (a, b, c))
    
if __name__ == '__main__':
    main()    
    