from Computer import calculate
from TestsUtils import passed

def testRequirmentCase():
  posY = 47.6
  posX = -122.4
  path = "coffee_shops_Coding_C.csv"
  actualResponse = [("Starbucks Seattle2",'0.0645'), ("Starbucks Seattle",'0.0861'), ("Starbucks SF",'10.0793')]
  assert str(calculate(posY, posX, path, True)) == str(actualResponse)
  passed("testRequirmentCase")


testRequirmentCase()
