import sys

def main():
    first = int(input("enter an integer: "))
    second = int(input("enter an integer: "))
    third = int(input("enter an integer: "))
    sum = first + second + third
    sum1 = first-second
    prod = third * first
    avg2 = sum / third
    print(f"{sum} {sum1} {prod} {avg2}")
if __name__ == "__main__":
    main()
