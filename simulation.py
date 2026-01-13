import random
deck = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"] * 4
target = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"] * 4
win_count = 0
loss_count = 0
position_count = 0
for j in range(1, 1000000):
  random.shuffle(deck)
  for i in range(1,52):
    if (target[i] == deck[i]):
      loss_count += 1
      position_count += i
      break
  else:
    win_count += 1
print(f"Wins: {win_count}\nLosses: {loss_count}\nAverage loss position: {position_count / loss_count}")
