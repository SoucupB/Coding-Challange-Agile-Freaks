import requests
from CSVValidator import validateCSVArray

def splitCSVArray(data):
  return [row.split(",") for row in data.split("\n")]

def latAndLonToFloat(rows):
  for row in rows:
    try:
      row[1] = float(row[1])
      row[2] = float(row[2])
    except Exception as error:
      print(repr(error))
      exit()
  try:
    validateCSVArray(rows)
  except Exception as error:
    print(repr(error))
    exit()
  return rows

def getCSVAsArray(path):
  response = requests.get(path)
  rows = splitCSVArray(response.text)
  return latAndLonToFloat(rows)

