def main():
    input_str = input("Enter a word or phrase: ")   # Get user input
    for i in range(len(input_str)):     # Loop through each character index in the input string
        if i % 2 == 0:  #even index gets uppercase
            print(input_str[i].upper(), end="")
        else:   #odd index gets lowercase
            print(input_str[i].lower(), end="")
    print()  # Print a newline at the end

    sentence_array = input_str.split(" ")
    for i in range(len(sentence_array)):    # Loop through each word index in the sentence array
        if i % 2 == 0: #even index gets uppercase
            sentence_array[i] = sentence_array[i].upper()
        else:   #odd index gets lowercase
            sentence_array[i] = sentence_array[i].lower()
    print(" ".join(sentence_array)) 
if __name__ == "__main__":
    main()
