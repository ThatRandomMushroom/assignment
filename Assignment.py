import sys
from dictionary import alpha
def main():
    ascinput = str(input("Write your text: \n>>> "))
    if ascinput == "":
        sys.exit()
    try:
        for row in range(len(alpha["a"])):
            for word in ascinput:
                print((alpha[word][row]), end=" ")
            print()
    except KeyError:
        print("You have entered a symbol that is not in the dictionary yet")


while True:
    if __name__ == "__main__":
        main()