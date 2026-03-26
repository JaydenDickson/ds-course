import sys

def hotel_cost(num_nights, city_flight = "new york"):
    '''Calculate hotel cost based on the number of nights and the city'''
    
    if clean_string(city_flight) == "new york":
        return num_nights * 150
    elif clean_string(city_flight) == "paris":
        return num_nights * 120
    elif clean_string(city_flight) == "tokyo":
        return num_nights * 100
    else:
        # If the city is not valid, exit the program with an error message
        sys.exit("Invalid city. Please choose from New York, Paris, or Tokyo.")
        


def plane_cost(city_flight):
    '''
    Calculate plane cost based on the city
    '''
    if clean_string(city_flight) == "new york":
        return 150
    elif clean_string(city_flight) == "paris":
        return 120
    elif clean_string(city_flight) == "tokyo":
        return 100
    else:
        return "Invalid city. Please choose from New York, Paris, or Tokyo."
def car_rental(rental_days):
    '''
    Calculate car rental based on the number of days a car will be rented
    '''
    return rental_days * 120

def holiday_cost(num_nights, city_flight, rental_days):
    '''
    Docstring for holiday_cost
    
    :param num_nights(Int): number of nights staying at the hotel
    :param city_flight(String): The city the user is flying to
    :param rental_days(Int): number of days the user will be renting a car
    '''
    # Calculate the total cost of the holiday by summing the hotel cost, plane cost, and car rental cost
    return hotel_cost(num_nights, city_flight) + plane_cost(city_flight) + car_rental(rental_days)


def clean_string(input_string):
    '''
    Clean the input string by removing leading and trailing whitespace and converting to lower case
    '''
    return input_string.strip().lower()

# Get user input for the holiday details
city_flight = input("Which city are you flying to? Choose from New York, Paris, or Tokyo: ")
num_nights = int(input("How many days will you be staying? "))
rental_days = int(input("How many days will you be renting a car? "))   
print("The total cost of your holiday is: $", holiday_cost(num_nights, city_flight, rental_days))