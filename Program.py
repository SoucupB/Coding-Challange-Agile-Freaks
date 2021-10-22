import sys
from CSVProcessor import getCSVAsArray

def processArguments():
  calculate(47.6, -122.4, "https://raw.githubusercontent.com/Agilefreaks/test_oop/master/coffee_shops.csv")

def calculate(userLatitude, userLongitude, path):
  coffeeShops = getCSVAsArray(path)
  print(coffeeShops)

processArguments()
