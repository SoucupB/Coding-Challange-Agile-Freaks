import sys
from CSVProcessor import getCSVAsArray
from MathProcessor import getDistance

def processArguments():
  calculate(47.6, -122.4, "https://raw.githubusercontent.com/Agilefreaks/test_oop/master/coffee_shops.csv")

def calculate(userLatitude, userLongitude, path):
  coffeeShops = getCSVAsArray(path)
  for shop in coffeeShops:
    print(getDistance(userLatitude, userLongitude, shop[1], shop[2]))
  print(coffeeShops)

processArguments()
