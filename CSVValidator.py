def validateCSVArray(rows):
  for row in rows:
    if len(row) != 3:
      raise Exception('Wrong number of columns in CSV')
    if validateLatitude(row[1]):
      raise Exception(f"Wrong latitude value for value {row[1]}")
    if validateLongitude(row[2]):
      raise Exception(f"Wrong longitude value for value {row[2]}")
  return True

def validateLatitude(latitude):
  return latitude < -90 or latitude > 90

def validateLongitude(longitude):
  return longitude < -180 or longitude > 180
