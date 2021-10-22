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
      raise Exception(f"One of the coordinates is malformed '{row[1]}' or '{row[2]}'!")
  validateCSVArray(rows)
  return rows

def getCSVAsArray(path):
  response = None
  if 'http://' in path or 'https://' in path:
    responseStructure = requests.get(path)
    if responseStructure.status_code != 200:
      raise Exception(f"This link leads nowhere")
    response = responseStructure.text
  else:
    try:
      with open(path) as fd:
        response = fd.read()
    except:
      raise Exception(f"This file does not exists check its spelling!")
  rows = splitCSVArray(response)
  return latAndLonToFloat(rows)

