from math import sqrt

#In orther to change the distance function to give min distance on a globe, just change this function.
def getDistance(posX_1, posY_1, posX_2, posY_2):
  return sqrt((posX_1 - posX_2) ** 2 + (posY_1 - posY_2) ** 2)
