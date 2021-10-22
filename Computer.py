from CSVProcessor import getCSVAsArray
from MathProcessor import getDistance
import heapq

def calculate(userLatitude, userLongitude, path, isTest=False):
  coffeeShops = getCSVAsArray(path)
  coffeeList = []
  response = []
  for shop in coffeeShops:
    distanceFromShop = getDistance(userLatitude, userLongitude, shop[1], shop[2])
    heapq.heappush(coffeeList, (distanceFromShop, shop[0]))
  numberOfCoffeeShops = 3
  for index in range(numberOfCoffeeShops):
    rootHeap = heapq.heappop(coffeeList)
    if not isTest:
      print(f"{rootHeap[1]},{'{:0.4f}'.format(rootHeap[0])}")
    response.append((rootHeap[1],'{:0.4f}'.format(rootHeap[0])))
  return response