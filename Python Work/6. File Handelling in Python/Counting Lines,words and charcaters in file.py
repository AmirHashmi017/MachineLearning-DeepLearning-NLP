#Read a text file and count the number of lines, words, and characters.
# Counting lines, words, and characters in a text file
with open("example.txt",'r') as file:
    lines=file.readlines()
    linecount=len(lines)
    wordcount=sum(len(line.split()) for line in lines)
    charachtercount=sum(len(line) for line in lines)
    print(f"Line Count: ",linecount)
    print(f"Words Count: ",wordcount)
    print(f"Characters Count: ",charachtercount)