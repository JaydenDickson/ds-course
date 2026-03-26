def main():
    total = 0
    user_input = 0
    number_valid_entries = 0
    while user_input != -1:
        user_input = int(input("Enter an integer:"))
        if user_input == 0:
            continue
        elif user_input == -1:
            break
        else:
            number_valid_entries += 1
            total += user_input
    print(total/number_valid_entries)     
                
if __name__ == "__main__":
    main()