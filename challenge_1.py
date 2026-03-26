import sys
import math

def main():
    a = float(input("Enter length of side a: "))
    b = float(input("Enter length of side b: "))
    c = float(input("Enter length of side c: "))

    s = (a + b + c) / 2  # semi-perimeter

    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    
    print("The area of the triangle is:", area)


if __name__ == "__main__":
    main()
