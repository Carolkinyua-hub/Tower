#Required Functions
#Be sure to add docstrings to all of your functions and comments to your code.

'''
1.You’ll run this function once at the beginning of the game.
-Creates a main pile of 60 bricks, represented as a list containing the integers 1 – 60.
-Creates a discard pile of 0 bricks, represented as an empty list.
-This function returns both lists.
-The method of returning 2 things from a function is to make a tuple out

2.Shuffle the given bricks (represented as a list). (You’ll do this to start the game.)
-This function does not return anything.
-You are allowed to import the random module and just use random.shuffle.
3.Check if there are any cards left in the given main pile of bricks.
-If not, shuffle the discard pile (using the shuffle function) and move those bricks to the
main pile.
-Then turn over the top card to be the start of the new discard pile.
4.
-Start the game by dealing two sets of 10 bricks each, from the given main_pile.
-Make sure that you follow the normal conventions of dealing. So, you have to
-deal one brick to the computer, one to the user, one to the computer, one to the
user, and so on.
-The computer is always the first person that gets dealt to and always plays first.
5.Sample 20 values from main pile
'''
import random
def setup_bricks():
 main_pile=list(range(1,61))
 discard_pile=[]
 bricks=(main_pile, discard_pile)
 def shuffle_bricks(main_pile):
  random.shuffle(main_pile)
  print("bricks=",bricks) 
 def sample(main_pile):
  sample_pile=list(random.sample(main_pile,21))
  print(len(sample_pile))
  print("sample_pile=",sample_pile)
  def deal_initial_bricks(sample_pile):
   computer_hand=list(sample_pile[0:10])
   user_hand=list(sample_pile[11:21])
   for i in range(len(computer_hand)):
    print("Computer_hand=",computer_hand[i])
    print(len(computer_hand)) 
   for x in user_hand:  
    print("User_hand=",user_hand[x])
    print(len(user_hand))
    deal_initial_bricks(sample_pile)
 shuffle_bricks(main_pile) 
 sample(main_pile)           
setup_bricks()
     