def main():
    #Input the file path.
    path = input("Enter the text file path: ")
    #Input the number of the most recent words to show.
    N = int(input("Number of the most recent words: "))
    try:
        #Open the file and do the Words scan.
        file = open(path, "r")
        WordsScanner(file, N)
    #In case the file wasn't found.
    except (FileNotFoundError, IOError):
        print("Could not open the file...")

# The scan function.
#Get file name an the number of most recent words.
def WordsScanner(file, N):
    #Define dictioanary for the words collection.
    WordsCollection = {}
    #Define array that will contain the file words.
    #Each word gets a index.
    FileWords = file.read().split()

    #Scan the array to collect all the words acording the number of appearances in the text.
    #key: word in the text, value: The number of appearances in the text
    for i in range(len(FileWords)):
        #if the word is already a key in the dictioanary.
        if FileWords[i] in WordsCollection.keys():
            #Add one more appearance (value+1).
            WordsCollection[FileWords[i]] += 1
        else:
            #Add the word as a new key and set the value to 1.
            WordsCollection[FileWords[i]] = 1

    #Sort all the words to a array.
    #First index is the most recent word.
    SortedCollection = sorted(WordsCollection.items(), key=lambda j: j[1], reverse=True)
    try:
        #print N of the most recent words.
        for k in range(N):
            print(SortedCollection[k])
    #In case the N is bigger then the array length.
    except IndexError:
        print("End of the list...")

    #Close the file.
    file.close()

#Active the main() function.
if __name__=="__main__":
    main()
    