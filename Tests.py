from Computer import calculate
from TestsUtils import passed

#The requirement testcase!
def testRequirmentCase():
  posY = 47.6
  posX = -122.4
  path = "coffee_shops_Coding_C.csv"
  actualResponse = [("Starbucks Seattle2",'0.0645'), ("Starbucks Seattle",'0.0861'), ("Starbucks SF",'10.0793')]
  assert str(calculate(posY, posX, path)) == str(actualResponse)
  passed("testRequirmentCase")

#Test the application to see if I change the users position to be closer to Sydney.
def testCloseToSydneyCase():
  posY = -35.871843
  posX = 150.206767
  path = "coffee_shops_Coding_C.csv"
  actualResponse = [('Starbucks Sydney', '2.2361'), ('Starbucks Moscow', '145.1768'), ('Starbucks Rio De Janeiro', '193.8741')]
  assert str(calculate(posY, posX, path)) == str(actualResponse)
  passed("testCloseToSydneyCase")

#Test if the application resonds with apropiate message if the input file does not exists.
def testNonExistentFileCase():
  posY = -35.871843
  posX = 150.206767
  path = "fakeFile.csv"
  try:
    calculate(posY, posX, path)
  except Exception as error:
    assert "This file does not exists" in str(error)
  passed("testNonExistentFileCase")

#Test if the provided link responds with correctly formatted data.
def testWrongLinkCase():
  posY = -35.871843
  posX = 150.206767
  path = "https://www.themuse.com/advice/the-35-best-personal-websites-weve-ever-seen"
  try:
    calculate(posY, posX, path)
  except Exception as error:
    assert "just not an CSV" in str(error)
  passed("testWrongLinkCase")

#Test if the data from the csv is correctly formatted. (the number are numbers and if there are 3 columns).
def testMalformedInputCase():
  posY = -35.871843
  posX = 150.206767
  path = "malformed.csv"
  try:
    calculate(posY, posX, path)
  except Exception as error:
    assert "One of the coordinates is malformed" in str(error)
  passed("testMalformedInputCase")

testRequirmentCase()
testCloseToSydneyCase()
testNonExistentFileCase()
testWrongLinkCase()
testMalformedInputCase()
print("Tests passed!")