import sys
from Computer import calculate
#python Program.py 47.6 -122.4 https://raw.githubusercontent.com/Agilefreaks/test_oop/master/coffee_shops.csv
#python Program.py 47.6 -122.4 coffee_shops_Coding_C.csv

def processArguments():
  if len(sys.argv) != 4:
    print("Wrong number of arguments!")
    return False
  try:
    posY = float(sys.argv[1])
    posX = float(sys.argv[2])
    link = sys.argv[3]
    shops = calculate(posY, posX, link)
    for shop in shops:
      print(f"{shop[0]},{shop[1]}")
    return True
  except Exception as error:
    if not isTest:
      print(error)
      exit()
    return False
  return None

processArguments()
