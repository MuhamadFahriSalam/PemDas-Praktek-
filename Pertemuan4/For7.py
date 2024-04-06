def main():
    data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    val = int(input('Masukkan nilai yang dicari: '))
    
    index = -1
    for i in range(len(data)):
        if data [i] == val:
            index = i
            break
    if index > -1:
        print('%d ditemukan pada indexs ke-%d' % (val, index))
        
    else:
        print('%d tidak ditemukan' % val)

if __name__ == '__main__':
    main()