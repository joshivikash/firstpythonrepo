n = int(input())
p1 = int(input())
p2 = int(input())
p3 = int(input())
if p1 > 0 and p2 > 0 and p3 > 0:
  if p1 != p2 and p2 != p3 and p1 != p3:
    if p1 + p2 + p3 == n:
      print("FAIR")
    else:
      print("UNFAIR")
  else:
    print("UNFAIR")
else:
  print("UNFAIR")