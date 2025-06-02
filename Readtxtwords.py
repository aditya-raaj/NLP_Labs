# No input(), just direct read
try:
    with open("C:/Users/Sowmya/Desktop/Sample.txt", "r") as file:
        content = file.read()
        words = content.split()
        print("Total number of words in the file:", len(words))
except FileNotFoundError:
    print("Error: File not found at the specified path.")
