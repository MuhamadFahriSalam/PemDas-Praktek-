def main():
    a = int(input('Masukkan bilangan bulat: '))
    if a > 0:
        print('%d adalah bilangan positif. ' % a)
    elif a == 0:
        print('Anda memasukan nilai nol. ')
    else:
        print('%d adalah bilangan negatif. ' % a)

if __name__ == '__main__':
    main()  