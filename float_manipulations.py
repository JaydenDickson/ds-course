import statistics
def main():
    input_num = [0.0 for i in range(10)]
    for i in range(10):
        input_num[i] = float(input("Enter a number: "))
    print("The total of the numbers is: ", sum(input_num)) #sum of the numbers
    print("The maximum index is: ", input_num.index(max(input_num))) #index of the maximum number
    print("The minimum index is: ", input_num.index(min(input_num))) #index of the minimum number
    print("The average of the numbers is: ", statistics.mean(input_num))
    print("The median of the numbers is: ", statistics.median(input_num))
if __name__ == "__main__":    
    main()