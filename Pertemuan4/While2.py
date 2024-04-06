import time

def main():
    i = 0
    while i < 5 :
        print('i=%d: Python' % i, end=', ')
        i +=1
        print('nilai i berubah menjadi %d' % i)
        
        time.sleep(5)

if __name__ == '__main__':
    main() 