import sys
from Computer import calculate
#python Program.py 47.6 -122.4 https://raw.githubusercontent.com/Agilefreaks/test_oop/master/coffee_shops.csv
#python Program.py 47.6 -122.4 coffee_shops_Coding_C.csv

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

processArguments(False)
