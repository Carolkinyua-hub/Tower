 '''def computer_play(computer_hand, discard_pile):
        ans=random.randint(0,1)
        if ans==0:
         computer_play=random.randint(0,9)
         replacing=computer_hand[computer_play]
         print("\n")
         #print("replacing",replacing,"with",i)
         print("computer played")
         computer_hand.remove(replacing)
         computer_hand.insert(computer_play,i)
        elif ans==1:
         discard_pile.append(i) 
       def user_tower(user_hand,discard_pile):
        print("user_hand=",user_hand,"\n")
        print("Want to use master_pile or discard_pile?\n")
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
          if user_hand==sorted(user_hand):
            print("winner is the User",user_hand)
            break
          elif computer_hand==sorted(computer_hand):
            print ("winner is the Computer",computer_hand)
            break
          else:
            continue
       user_tower(user_hand,discard_pile)  
       computer_play(computer_hand,discard_pile)
 '''