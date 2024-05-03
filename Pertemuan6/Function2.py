import os

def clearScreen():
    os.system('clear')

def echo(s):
    print(s)

def main():
    clearScreen()
    echo('Pyhton 3')
    
if __name__ == '__main__':
    main()