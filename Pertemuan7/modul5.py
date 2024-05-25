import constants
import writer

def kali(a, b):
    return a * b

def main():
    writer.printA()
    writer.printB()
    print('A x B = %d' % kali(constants.A, constants.B))
    
if __name__ =='__main__':
    main()