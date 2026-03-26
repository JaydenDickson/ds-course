import sys

def main():
    sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."
    print(sentence.replace("!", " "))
    print(sentence.upper())
    print(sentence[::-1])
if __name__ == "__main__":
    main()
