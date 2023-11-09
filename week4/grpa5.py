import math

n = int(input())
points = []
while n > 0:
  points.append(input())
  n -= 1
p = input()
dist = []
min_dist = 1001
for i in range(len(points)):
  x = p.split(',')[0]
  y = p.split(',')[1]
  x1 = points[i].split(',')[0]
  y1 = points[i].split(',')[1]
  d = math.sqrt((float(x) - float(x1))**2 + (float(y) - float(y1))**2)
  dist.append(d)
  if (d < min_dist):
    min_dist = d

for i in range(len(dist)):
  if (dist[i] == min_dist):
    print(points[i])
