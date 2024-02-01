"""
Welcome to the Holiday Planner! 🌴✈️

Are you dreaming of a perfect getaway? Let's plan your holiday with this user-friendly script.

Simply enter your desired holiday details, and we'll calculate the costs for you!

Where are you looking to go on holiday? Choose from these fantastic destinations: London, Paris, or Barcelona.

"""

# created a list of valid citys only
valid_cities = ['London', 'Paris', 'Barcelona']

# this while loop provides validation for the user input for the city name.
while True:
    city_flight = input("Please enter the city you will be flying to (London, Paris, Barcelona): ")
    if city_flight.capitalize() in valid_cities:
        break  # Break the loop if the input is valid
    else:
        print("Invalid city. You entered:", city_flight)
        print("Please try again:")

num_nights = int(input("The number of nights you will be staying at a hotel: "))

rental_days = int(input("The number of days for which you will be hiring a car: "))

# This function calculates Hotel costs
def hotel_cost(number_of_nights, per_night=100):  
    total = number_of_nights * per_night
    return total

# This function calculates Plane costs
def plane_cost(city_flight):
    if city_flight == 'London':
        return 190
    elif city_flight == 'Paris':
        return 250  # Adjusted cost for Paris
    elif city_flight == 'Barcelona':
        return 200
    else:
        print("You have entered an invalid flight city.")
        return 0

# This funcion calculates Car costs
def car_rental(rental_days, daily_rentals=50):
    total = rental_days * daily_rentals
    return total

# Functon to calculate Hotel costs total
def holiday_costs(number_of_nights, city_flight, rental_days):
    total_hotel_costs = hotel_cost(number_of_nights)
    total_plane_costs = plane_cost(city_flight)
    total_car_rental_costs = car_rental(rental_days)

    total_costs = total_hotel_costs + total_plane_costs + total_car_rental_costs
    return total_hotel_costs, total_plane_costs, total_car_rental_costs, total_costs

# Corrected function call using the correct variable names
hotel, plane, car, Total_costs = holiday_costs(num_nights, city_flight, rental_days)

# Print individual costs
print("\nIndividual Costs:")
print("Hotel Cost: £", hotel)
print("Plane Cost: £", plane)
print("Car Rental Cost: £", car)

print("\nThe total for your holiday is: £", Total_costs)