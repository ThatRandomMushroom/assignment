letters = {
    "a": [
        "  ##  ",
        " #  # ",
        "#    #",
        "######",
        "#    #",
        "#    #",
    ],
    "b": [
        "##### ",
        "#    #",
        "##### ",
        "#    #",
        "#    #",
        "##### ",
    ]
}

str = input("Please enter a value")
for row in range(len(letters['a'])):
    for letter in str:
        print(letters[letter][row], end="  ")
    print()
