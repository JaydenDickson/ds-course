def main():
    swim = int(input("enter swimming time:"))
    cycle = int(input("enter cycle time:"))
    run = int(input("enter running time:"))
    sum = swim + cycle + run
    print("Award:")
    if sum  <= 100:
        print("Provincial colours")
    elif sum <= 105:
        print("Provincial half colours")
    elif sum <= 110:
        print("Provincial Scroll")
    else:
        print("No award")

if __name__ == "__main__":
    main()