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
  sample_pile=list(random.sample(main_pile,20))
  print("sample_pile=",sample_pile)
  print("length=",len(sample_pile))
  def main_piles(main_pile, sample_pile):
   for i in main_pile[:]:
    if i in sample_pile:
     main_pile.remove(i)
  main_piles(main_pile, sample_pile)
  def deal_initial_bricks(sample_pile):
   computer_hand=sample_pile[0:10]
   user_hand=sample_pile[10:21]
   print("Computer_hand=",computer_hand)
   print(len(computer_hand))
   print("User_hand=",user_hand)
   print(len(user_hand))
   print("main_pile=",len(main_pile))
   #print("main_pile=",main_pile)  
   def play(user_hand,main_pile,discard_pile):
    options=list(main_pile[0:40])
    for i in options:
     ans=random.randint(0,1)
     if ans==0:
      computer_play=random.randint(0,9)
      replacing=computer_hand[computer_play]
      print("replacing",replacing,"with",i)
      computer_hand.remove(replacing)
      computer_hand.insert(computer_play,i)
      print("Computer_hand:",computer_hand)
     elif ans==1:
      discard_pile.append(i) 
      print("Want to use master_pile or discard_pile?")
      option=input("option1:/option2:?")
     if option=="option1":
      print("Want to use:",i)
      answer=input('yes/no')
      if answer=="yes":
        print("choose a position\n")
        print("indexed from 0-9 respectively\n:")
        position=input("location:0-9:")
        ind=int(position)
        print(ind)
        replaced=user_hand[ind]
        print("replacing:",replaced,"with",i)
        user_hand.remove(replaced)
        user_hand.insert(ind,i)
        print("user_hand=",user_hand)
     elif option=="option2":
        for x in discard_pile[:]:
         print("Choice:",x)
         print("choose a position\n")
         print("indexed from 0-9 respectively\n:")
         position=input("location:0-9:")
         ind=int(position)
         print(ind)
         replaced=user_hand[ind]
         print("replacing:",replaced,"with",i)
         user_hand.remove(replaced)
         user_hand.insert(ind,i)
         print("user_hand=",user_hand)
   play(user_hand,main_pile,discard_pile)
  deal_initial_bricks(sample_pile)
 shuffle_bricks(main_pile) 
 sample(main_pile)           
setup_bricks()
     