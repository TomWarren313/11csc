#function to get data
def getData():
    car = input('Please enter a car brand: ').title()
    return car

#function that deals with processing and sorting the dictionary
def processing():
  car_brands = {}
  flag = True
  while flag:
    key = getData()
    if key == '':
        flag = False
        return car_brands
#If something is already in dictionary, value gets + 1, if it isn't in the dictionary it gets added with a value of one
    elif key in car_brands:
        car_brands[key] += 1
    else:
        car_brands[key] = 1
#function that is used to get our output and print it
def output():
  my_car_brands = processing()
  for key,value in my_car_brands.items():
#I prefer to use commas instead of f-strings as it looks more precise
    print(key, 'has been entered', value, 'time(s)')

#main routine
output()