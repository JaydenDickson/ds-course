def main():
    name = input("What is your name? ")
    age = input("What is your age? ")
    housenumber = input("What is your house number? ")
    street = input("What is your street? ")

    print(
        "This is {}. He is {} years old and lives at house number {} on {}."
        .format(name, age, housenumber, street)
    )


if __name__ == "__main__":
    main()
