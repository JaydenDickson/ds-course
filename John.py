def main():
    user_input = ""
    list_names = []
    while "".join(user_input.strip().lower().split()) != "john":
        user_input = input("Enter your name: ")
        if "".join(user_input.strip().lower().split()) == "john":
            break
        else:
            list_names.append("".join(user_input.strip().lower().split()))
    print(list_names)
if __name__ == "__main__":
    main()