def main():
    a = int(input('Masukkan Bilangan bulat: '))
    
    if a % 2 == 0:
        print('%d adalah bilangan genap.' % a)
    else:
        print('%d adalah bilangan ganjil.' % a)
    
if __name__ == '__main__':
    main()  