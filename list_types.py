def main():
    friends_names = ["Rachel", "Michael", "Abdul"]
    print(friends_names[0], friends_names[2], len(friends_names))
    friends_ages = [21,22,23]
    for i in range(len(friends_names)):
        print(friends_names[i], "is", friends_ages[i], "years old.")
if __name__ == "__main__":
    main()