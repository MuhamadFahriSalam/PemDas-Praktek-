def kali(a, b):
    return a * b

def echo(s, n):
    for i in range(n):
        print(s)
def main():
    print('Pemanggilan pertama fungsi kali():')
    print('2 x 3 = %d' % kali(2, 3))
    
    print('Pemanggilan kedua fungsi kali():')
    print('10 x 20 = %d' % kali(10, 20))
    
    
    print('\nPemanggilann pertama fungsi echo():')
    echo('Python', 5)
    
    print('\nPemanggilann kedua fungsi echo():')
    echo('Pemograman pyhon', 3)
    
if __name__== '__main__':
    main()
    