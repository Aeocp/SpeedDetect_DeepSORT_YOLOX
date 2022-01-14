def createLine():
  numLine = int(input("Enter number of counting line :"))
  x = []
  y = []
  print("Enter the beginning and ending of the line (0-1) (xb,yb,xe,ye) :")
  for l in range(numLine):
    print("Line",l+1)
    Bp = input("Enter line position :").split(",")
    x.append((Bp[0]))
    y.append((Bp[1]))
    x.append((Bp[2]))
    y.append((Bp[3]))
  return numLine,x,y

def createLineSpeed():
  x1 = []
  y1 = []
  x2 = []
  y2 = []
  print("Enter the beginning and ending of two line (0-1) (xb1,yb1,xe1,ye1,xb2,yb2,xe2,ye2)")
  Bp = input("Enter line position :").split(",")
  x1.append((Bp[0]))
  y1.append((Bp[1]))
  x1.append((Bp[2]))
  y1.append((Bp[3]))
  x2.append((Bp[4]))
  y2.append((Bp[5]))
  x2.append((Bp[6]))
  y2.append((Bp[7]))
  return x1,y1,x2,y2
