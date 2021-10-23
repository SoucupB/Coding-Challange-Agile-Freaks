def validateCSVArray(rows):
  for row in rows:
    if validatePosY(row[1]):
      raise Exception(f"Wrong PosY value for value {row[1]}")
    if validatePosX(row[2]):
      raise Exception(f"Wrong PosX value for value {row[2]}")
  return True

def validatePosY(PosY):
  return PosY < -90 or PosY > 90

def validatePosX(PosX):
  return PosX < -180 or PosX > 180
