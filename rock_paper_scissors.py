import random
'''Rock,
   paper
   scissor'''

hilter = {"r":-1,"p":0,"s":1}
reverse_hilter = {-1:"Rock",0:"Paper",1:"Scissor"}
while True:
     user = input('chose rock,paper, scissor. r/p/s: ').lower().strip()
     
     if user not in hilter:
        print("Invalid input,try again.")
        continue
     
     user_val = hilter[user]
     comp_val = random.choice([-1,0,1])

     print(f"computer chose: {reverse_hilter[comp_val]}")

     if user_val == comp_val:
         print("Its a draw")
     elif (user_val - comp_val) in [-2, 1]:
        print("You win!")
     else:
        print("You lose!")

 #ask to continue
     again = input("play again? y/n: ")
     if again == 'n':
         print("Thanks for playing! Goodbye")
         break
