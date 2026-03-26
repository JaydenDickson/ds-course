def main():
    menu = ["soup", "salad", "sandwich", "pasta"]
    stock = {"soup": 10, "salad": 5, "sandwich": 7, "pasta": 3}
    price = {"soup": 3.99, "salad": 4.99, "sandwich": 5.99, "pasta": 6.99}
    total_stock = []
    for item in menu:
        total_stock.append(stock[item] * price[item])
    print(total_stock)

if __name__ == "__main__":
    main()