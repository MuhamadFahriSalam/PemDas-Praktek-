def main():
    c = input('Masukkan huuruf: ')[0].lower()
    
    if c in ['a', 'e', 'i', 'o', 'u']:
        print('%c adalah huruf vocal' % c)
    
if __name__ == '__main__':
    main()