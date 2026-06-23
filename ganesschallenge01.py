def get_data(car_brands):
    car = input('Please enter a car brand: ').title()
    if car != '':
        if car in car_brands:
            car_brands[car] += 1
        else:
            car_brands[car] = 1
    return car  # Returns the car name so we can check if it's empty

def processing():
    car_brands = {}
    while True:
        # Pass the dictionary into get_data so it gets updated
        new_car = get_data(car_brands)
        if new_car == '':
            break
    return car_brands

def output(my_car_brands):
    # Loop over the dictionary passed as a parameter
    for key, value in my_car_brands.items():
        print(key, 'has been entered', value, 'time(s)')

# Main Routine
# Create the dictionary here, then pass it through the functions
final_brands = processing()
output(final_brands)