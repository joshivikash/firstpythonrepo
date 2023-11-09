import random

rolls = []
for i in range(100000):
  # randint includes the endpoints
  roll = random.randint(1, 6)
  rolls.append(roll)
print(len(rolls))
count = 0
primes = [2, 3, 5]
for roll in rolls:
  if roll in primes:
    count += 1
print(count)
