import sys
from CSVProcessor import getCSVAsArray
from MathProcessor import getDistance
import heapq

#python Program.py 47.6 -122.4 https://raw.githubusercontent.com/Agilefreaks/test_oop/master/coffee_shops.csv

def processArguments(isTest):
  if len(sys.argv) != 4:
    raise Exception("Wrong number of arguments!")
  try:
    posY = float(sys.argv[1])
    posX = float(sys.argv[2])
    link = sys.argv[3]
    calculate(posY, posX, link, isTest)
    return True
  except Exception as error:
    if not isTest:
      print(error)
      exit()
    return False
  return None

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
    response.append(rootHeap)
  return response

processArguments(False)
