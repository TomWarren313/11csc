favourites = {}

brand = input('brand: ')
while brand:
  favourites[brand]
  brand = input('brand: ')

for brand in favourites:
  print(brand, favourites[brand])