import math

def luasLingkaran(r):
    def kuadrat(x):
        return x ** 2
    return math.pi * kuadrat(r)

def main():
    r  = float(input('Masukkan jari-jari linggkaran: '))
    
    luas = luasLingkaran(r)
    
    print('Luas lingkaran = %.3f' % luas)
    
if __name__== '__main__':
    main()