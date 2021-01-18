#Estou utilizando um código de calculo balístico de projéteis de morteiro em um mapa de grade genérico de um terreno para fim de aprendizado
import math
import os

clear = lambda: os.system('cls')

#################################################################
# Constantes
CARDINAL_DIRECTIONS = ("N", "NE", "E", "SE", "S", "SW", "W", "NW")
GRID_SIZE = 300; # Distância (meters) de um mapa de malha.

# Tabela de conversões.
DISTANCES = (50,100,150,200,250,300,350,400,450,500,550,600,650,700,750,800,850,900,950,1000,1050,1100,1150,1200,1250)
MILS      = (1579,1558,1538,1517,1496,1475,1453,1431,1409,1387,1364,1341,1317,1292,1267,1240,1212,1183,1152,1118,1081,1039,988,918,800)
# fim das constantes
#################################################################

def convertCoordinate(stringInput):
  if len(stringInput) < 2:
    print ("Input Error: " + stringInput)
    return
  
  x = int(ord(stringInput[0].lower())-ord("a"))*GRID_SIZE
  y = (int(stringInput[1])-1)*GRID_SIZE
  
  if len(stringInput) == 2:
    x += GRID_SIZE / 2;
    y += GRID_SIZE / 2;
  else:
    keypadSize = GRID_SIZE
    for i in range(2,len(stringInput), 2):
      keypadSize /= 3 # Shrink keypad size by factor of 3
      keypad = int(stringInput[i+1])
      
      # Add X Component of (Sub)Keypad\
      if keypad == 2 or keypad == 5 or keypad == 8:
        x += keypadSize
      elif keypad == 3 or keypad == 6 or keypad == 9:
        x += 2*keypadSize
        
      # Add Y Component of (Sub)Keypad
      if keypad == 4 or keypad == 5 or keypad == 6:
        y += keypadSize
      elif keypad == 1 or keypad == 2 or keypad == 3:
        y += 2*keypadSize
    
    # Center point in (Sub)Keypad
    x += keypadSize / 2
    y += keypadSize / 2
  
  #print stringInput + " (" + str(int(round(x))) + ", " + str(int(round(y))) + ")"
  return (x,y);

# Calculates the distance between two points.
def calcDistance(coord1, coord2):
  return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def calculateVectorMagnitude(vector):
  return math.sqrt(vector[0]**2 + vector[1]**2)

# Calculates the degrees from north (clockwise) of mortarCoord to targetCoord
def calcAzimuth(mortarCoord, targetCoord):
  # Target Vector
  targetVector = (targetCoord[0] - mortarCoord[0], targetCoord[1] - mortarCoord[1])
  
  # Calculate Unit Circle Quadrant and add offset
  tempVector = (0, -1)
    
  # Dot Product of Temp Vector & Target Vector
  product = tempVector[0] * targetVector[0] + tempVector[1] * targetVector[1]
  angle = math.acos(product / (calculateVectorMagnitude(tempVector) * calculateVectorMagnitude(targetVector)))
  
  degrees = math.degrees(angle)
  
  if targetVector[0] < 0:
    degrees = 180 + (180-degrees)
  
  return degrees;

# The elevation to milliradian conversion is not strictly linear.
# The values between the given ranges on the chart will be linearly
# interpolated using the values.
def calcElevation(distance):
  if distance < DISTANCES[0]:
    return "Out of Range (<" + str(DISTANCES[0]) + "m)"
  elif distance > DISTANCES[-1]:
    return "Out of Range (>" + str(DISTANCES[-1]) + "m)"
  else:
    for i, value in enumerate(DISTANCES):
      #print str(i) + "\t" + str(value) + "\t" + str(MILS[i])
      if distance == value:
        return str(MILS[i])
      elif distance < value:
        m = (MILS[i] - MILS[i-1]) / (DISTANCES[i] - DISTANCES[i-1]);
        return str(int(m * (distance - DISTANCES[i]) + MILS[i]))
  
  return "UNEXPECTED ERROR"

def convertDegreeToCardinal(degree):
  if int(degree) % 45 == 0:
    return str(CARDINAL_DIRECTIONS[int(int(degree) / 45)])
  else:
    return str(degree) + "°"

def startTargetLoop():
  mortarCoordinate = input("Mortar Coordinate: ") # todo: error handle this coordinate input.
  mortarPosition = convertCoordinate(mortarCoordinate)
  
  targetCoordinate = ""
  while targetCoordinate != "x":
    # Wait for new input
    targetCoordinate = str(input("Target Coordinate: "))
    clear()
    
    if targetCoordinate.lower() == "x":
      return
    elif targetCoordinate == "?":
      printHelp()
    else:
      # Calculate Components
      targetPosition = convertCoordinate(targetCoordinate)
      distance = calcDistance(mortarPosition, targetPosition)
      angle = calcAzimuth(mortarPosition, targetPosition)
      
      # Output Results
      print ("Type X to return to main menu.")
      print ("")
      print ("Mortar: " + mortarCoordinate + "\tTarget: " + targetCoordinate)
      print ("(" + str(mortarPosition[0]) + "," + str(mortarPosition[1]) + ")\t(" + str(targetPosition[0]) + "," + str(targetPosition[1]) + ")")
      print ("Distance:\t" + str(round(distance)) + "m")
      print ("")
      print ("Azimuth:\t" + convertDegreeToCardinal(round(angle)))
      print ("Elevation:\t" + calcElevation(distance) + "mils")
      print ("")
    
  clear()

while True:
  print ("")
  print ("Main Menu")
  print ("1 - Start Calculator")
  print ("3 - Run debug cases")
  print ("? - Show help from any menu.")
  print ("")
  
  selectedOption = input("Selection: ")
  print ("")

  if selectedOption == "?":
    printHelp()
  elif selectedOption == "1":
    startTargetLoop()
  elif selectedOption == "3":
    print ("Angle between B2 and C1: " + str(calcAzimuth(convertCoordinate("B2"), convertCoordinate("C1"))))
    print ("Angle between B2 and C3: " + str(calcAzimuth(convertCoordinate("B2"), convertCoordinate("C3"))))
    print ("Angle between B2 and A3: " + str(calcAzimuth(convertCoordinate("B2"), convertCoordinate("A3"))))
    print ("Angle between B2 and A1: " + str(calcAzimuth(convertCoordinate("B2"), convertCoordinate("A1"))))
    print
    print ("Elevation 25m: " + calcElevation(25))
    print ("Elevation 1500m: " + calcElevation(1500))
    print ("Elevation 750m: " + calcElevation(750))
    print ("Elevation 775m: " + calcElevation(775))