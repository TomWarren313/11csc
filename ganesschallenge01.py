'''
Function that gets user data
'''
def getData(car_brand):
    car = input('car brand: ').title()
    if car != '':
        if car in car_brand:
            car_brand[car] += 1
        else:
            car_brand[car] = 1
    return car 
'''
Function that proccesses
'''
def processing():
    car_brand = {}
    flag = True
    while flag:
        new_car = getData(car_brand)
        if new_car == '':
            flag = False
    return car_brand
'''
Function that outputs
'''
def output(my_car_brands):
    # Loops
    for key, value in my_car_brands.items():
        print(key, 'has been entered', value, 'time(s)')
#main routine
f_brands = processing()
output(f_brands)