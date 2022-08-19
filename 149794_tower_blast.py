#149794
#Nyaguthii Kinyua
#Declaration:This is my original work, with no assistance
import random
def main():
 if __name__=="__main__":
  #Set up Building Materials
  def setup_bricks():
   '''This function aims to create two lists(The main and discard pile) and a constituent tuple''' 
   main_pile=list(range(1,61))
   bricks=[]
   discard_pile=[]
   user_hand=[]
   computer_hand=[]
   brick_pile=[]
   optimum=[] 
   maximum=[]
   bricks.append(main_pile)
   bricks.append(discard_pile)
   bricks=tuple(bricks)
  #Randomization initialization
   def shuffle_bricks(bricks):
    '''This function shuffles bricks'''
    random.shuffle(bricks)
    print("bricks=",bricks,"\n") 
   def sample(main_pile):
    '''This is meant to randomly sample 20 datapoints from the main pile'''
    sample_pile=list(random.sample(main_pile,20))
    print("sample_pile=",sample_pile,"\n")
    print("Sample_pile length=",len(sample_pile),"\n")
    def main_piles(main_pile, sample_pile):
     '''This aims at removing the randomly selected sample pile data points from the main pile'''
     for i in main_pile[:]:
      if i in sample_pile:
       main_pile.remove(i)
    main_piles(main_pile, sample_pile)
    def deal_initial_bricks(sample_pile):
     ''' This allows for the dealing of the randomized sample data to the two players'''
     for j in sample_pile[0:10]:
      computer_hand.append(j)
     for i in sample_pile[10:20]:
      user_hand.append(i)
     #Assigns 10 points to each player
     print("Computer_hand=",computer_hand,"\n")
     print("Computer assigned",len(computer_hand),"bricks.")
     print("\n")
     print("User_hand=",user_hand,"\n")
     print("User assigned",len(user_hand),"bricks.")
     print("\n") 
    def check_bricks(main_pile,discard_pile):  
      '''This fxn aims to replace an empty main_pile from shuffled discard_pile'''
      if (len(main_pile))==0:
       print("main_pile length",len(main_pile))
       random.shuffle(discard_pile)
       main_pile.append(discard_pile)
       print("Appended from discard_pile")
       print("\n") 
    def add_brick_to_discard(main_pile,discard_pile):
      '''This fxn aims to add empty discard_pile from top val from main_pile'''
      if (len(discard_pile))==0:
       print("To discard_pile append,",main_pile[0])
       discard_pile.append(main_pile[0])
       main_pile.remove(main_pile[0])
       print("\n")
       print("\n")
       print("main_pile",main_pile)
       print("\n")
       print("Length of main_pile=",len(main_pile),"\n")
    def get_top_brick(brick_pile):# computer_hand,main_pile,discard_pile):
     brick_pile.append(user_hand[0])
     brick_pile.append(computer_hand[0])
     brick_pile.append(main_pile[0])
     brick_pile.append(discard_pile[0])
     print("All top values are:", brick_pile)
     print("\n")
     print("Top val in user_hand is",brick_pile[0])
     print("\n")
     print("Top val in computer_hand is",brick_pile[1])
     print("\n")
     print("Top val in main_pile is",brick_pile[2])
     print("\n")
     print("Top val in discard_pile is",brick_pile[3])
     print("\n")
    def play(computer_hand,main_pile,discard_pile):
      def computer_play(brick_pile,computer_hand,main_pile,discard_pile):
       '''Strategy to randomly select to pick from either piles'''
       #generate random for option 0,1 for master and discard pile respctively
       ans=random.randint(0,1)
       if ans==0:
        opt=random.randint(2,3)
        if opt==2:
         print("Insert to Comp Tower",brick_pile[2])
         #find position of minimum value in computer_pile in comparison to the top most item in the 
         def get_optimum(computer_hand):
          for r in computer_hand:
           if r<brick_pile[2]:
            optimum.append(r)
         get_optimum(computer_hand)
         def get_maximum(computer_hand,optimum):
           maximum.append(max(optimum))
           print(maximum) 
           maxs=maximum[0]
           for t in computer_hand:
            if t==maxs:
             index=(computer_hand.index(t)+1)
             print(index)
             val_ind=computer_hand[index]
             computer_hand.remove(val_ind)
             computer_hand.insert(index,brick_pile[2])
             discard_pile.append(maxs)
             print(computer_hand)
         get_maximum(computer_hand,optimum)
        else: 
          print("No insert for computer Tower")
          print("user_hand=",user_hand,"\n")
          print("Want to use master_pile or discard_pile?\n")
          for i in main_pile:
           option=input("option1 or option2 :")
           print("\n")
           if option=="option1":
            print("\n")
            print("Want to use:",i)
            print("\n")
            answer=input('yes/no:')
            print("\n")
            if answer=="yes":
             print("choose a position\n")
             print("indexed from 0-9 respectively\n")
             position=input("location:0-9:")
             print("\n")
             ind=int(position)
             print("\n")
             print(ind)
             print("\n")
             replaced=user_hand[ind]
             print("replacing:",replaced,"with",i,"\n")
             user_hand.remove(replaced)
             user_hand.insert(ind,i)
             print("user_hand=",user_hand,"\n")
            elif answer=="no":
             discard_pile.append(i) 
            elif option=="option2":
             for x in discard_pile[:]:
              print("Choice:",x,"\n")
              print("choose a position\n")
              print("indexed from 0-9 respectively\n:")
              position=input("location:0-9:\n")
              ind=int(position)
              print(ind)
              replaced=user_hand[ind]
              print("replacing:",replaced,"with",x,"\n")
              user_hand.remove(replaced)
              user_hand.insert(ind,x)
              print("user_hand=",user_hand)  
       elif ans==1:
         for d in discard_pile[:]:
            print("Choice:",d,"\n")
            computer_plays=random.randint(0,9)
            positions=computer_plays
            inds=int(positions)
            print(inds)
            replaced=user_hand[inds]
            print("replacing:",replaced,"with",d,"\n")
            user_hand.remove(replaced)
            user_hand.insert(inds,d)
            print("user_hand=",user_hand) 
      computer_play (brick_pile,computer_hand,main_pile,discard_pile)
    check_bricks(main_pile,discard_pile) 
    add_brick_to_discard(main_pile,discard_pile)   
    deal_initial_bricks(sample_pile)
    get_top_brick(brick_pile)
    play(computer_hand,main_pile,discard_pile)
   shuffle_bricks(main_pile) 
   sample(main_pile)         
 setup_bricks()
main()  
