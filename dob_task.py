def main():
    with open("./DOB.txt", "r") as file:
        data = file.readlines()

        for line in data:
            parts = line.strip().split(" ")
            print(parts[0], parts[1])

        for line in data:
            parts = line.strip().split(" ")
            print(parts[2], parts[3], parts[4])


if __name__ == "__main__":
    main()
