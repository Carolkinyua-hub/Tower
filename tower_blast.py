#149794
#Nyaguthii Kinyua
#Declarion:This is my original work, with no assistance
import random
def main():
 if __name__=="__main__":
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
     def tower(user_hand, computer_hand,main_pile,discard_pile):
      options=list(main_pile[0:40])
      for i in options:
       def computer_play(computer_hand, discard_pile):
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
       def user_tower(user_hand,discard_pile):
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
         elif answer=="no":
          discard_pile.append(i) 
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
       user_tower(user_hand,discard_pile)  
       computer_play(computer_hand,discard_pile)
     tower(user_hand,computer_hand,main_pile,discard_pile) 
    deal_initial_bricks(sample_pile)
   shuffle_bricks(main_pile) 
   sample(main_pile)           
 setup_bricks()
main()  
