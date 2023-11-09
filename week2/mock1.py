nos_of_coins = int(input())
coins_with_p1 = int(input())
coins_with_p2 = int(input())
coins_with_p3 = int(input())
total_coins_given = coins_with_p1 + coins_with_p2 + coins_with_p3
if(nos_of_coins - total_coins_given != 0):
  print('UNFAIR')
elif(coins_with_p1 == 0 or coins_with_p2 == 0 or coins_with_p3 == 0):
  print('UNFAIR')
elif(coins_with_p1 == coins_with_p2 or coins_with_p3 == coins_with_p2 or coins_with_p1 == coins_with_p3):
  print('UNFAIR')
else:
  print('FAIR')