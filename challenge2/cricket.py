class Player:
 def play(self):
  print("The player is playing Cricket") 
class Batsman (Player):
 def play(self):
   print("The batsman is batting")
class Bowler (Player):
 def play(self): print("The bowler is Bowling")
batsman=Batsman()
bowler=Bowler()
batsman.play()
bowler.play()