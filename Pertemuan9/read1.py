def main():
    f = open('data.txt', 'r')
    
    data = f.read()
    
    rawData = data.encode('unicode-escape')
    
    print(rawData)
    
    f.close()
    
if __name__ == '__main__':
    main()
    