def main():
    #In the exercise called pattern.py, the following code does not produce the desired result
    for i in range(11):
        for j in range(abs(6-i),6):
            print("*", end="")
        print("")
if __name__ == "__main__":
    main()