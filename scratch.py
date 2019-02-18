import sys
from dictionary import alpha
running = True
def main():
    ascinput = str(input("Write your text: \n>>> "))
    if ascinput == "":
        sys.exit()
    for row in range(len(alpha["a"])):
        for word in ascinput:
            print((alpha[word][row]), end=" ")
        print()

if __name__ == "__main__":
    main()

while True:
    main()