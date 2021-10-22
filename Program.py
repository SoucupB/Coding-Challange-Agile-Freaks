import sys
from CSVProcessor import getCSVAsArray
from MathProcessor import getDistance
import heapq

def processArguments():
  calculate(47.6, -122.4, "https://raw.githubusercontent.com/Agilefreaks/test_oop/master/coffee_shops.csv")

def calculate(userLatitude, userLongitude, path):
  coffeeShops = getCSVAsArray(path)
  coffeeList = []
  for shop in coffeeShops:
    distanceFromShop = getDistance(userLatitude, userLongitude, shop[1], shop[2])
    heapq.heappush(coffeeList, (distanceFromShop, shop[0]))
  numberOfCoffeeShops = 3
  for index in range(numberOfCoffeeShops):
    rootHeap = heapq.heappop(coffeeList)
    print(f"{rootHeap[1]},{'{:0.4f}'.format(rootHeap[0])}")

processArguments()
