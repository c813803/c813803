import random
suits=(u"\u2664",u"\u2661",u"\u2662",u"\u2667")                   #宣告 方塊 梅花 
ranks=("A","2","3","4","5","6","7","8","9","10","J","Q","K")
pokers=[(i,j) for i in suits for j in ranks]
#########################
random.shuffle(pokers)
#print(pokers)
#########################
players=[[],[],[],[]]
y=[]
while len(pokers) != 0:
  for i in range(1,5 ):
     players[i].append(pokers[len(pokers)-1])
       pokers.pop()
  for i in range(4):
       print("第{}位玩家 = ".format(i+1),end=" ")
  for card in players[i]:
       print(" ".join(card), end=" , ")
  print()
