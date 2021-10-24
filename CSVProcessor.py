import requests
from CSVValidator import validateCSVArray

def splitCSVArray(data):
  return [row.split(",") for row in data.split("\n")]

def pointsIntegrity(rows):
  for row in rows:
    if len(row) != 3:
      raise Exception('Wrong number of columns in CSV or just not an CSV')
    try:
      row[1] = float(row[1])
      row[2] = float(row[2])
    except Exception as error:
      raise Exception(f"One of the coordinates is malformed '{row[1]}' or '{row[2]}'!")
  validateCSVArray(rows)
  return rows

def getCSVAsArray(path):
  response = None
  if 'http://' in path or 'https://' in path:
    try:
      responseStructure = requests.get(path)
      if responseStructure.status_code != 200:
        raise Exception()
      response = responseStructure.text
    except Exception as error:
      raise Exception(f"This link leads nowhere or data is not a csv")
  else:
    try:
      with open(path) as fd:
        response = fd.read()
    except:
      raise Exception(f"This file does not exists check its spelling!")
  rows = splitCSVArray(response)
  return pointsIntegrity(rows)

