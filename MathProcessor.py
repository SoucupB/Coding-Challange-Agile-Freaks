from math import sqrt

#In orther to change the distance function to give min distance on a globe, just change this function.
def getDistance(lat1, lon1, lat2, lon2):
  return sqrt((lat1 - lat2) ** 2 + (lon1 - lon2) ** 2)
