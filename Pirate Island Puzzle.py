import time
def pirate_island_puzzle():
 print("☠")
 time.sleep(1)
 print("Welcome to my island!")
 time.sleep(1)
 print("There is two doors in front of you. 🚪 a red door and 🚪 a blue door")
 time.sleep(1)
 door = input("Which door do you want to open? \n").lower()
 while door != "red" and door != "blue":
   print ("Sorry, Inavlid choice! 🤷‍♂️🤷‍♂️🤷‍")
   time.sleep(1)
   door = input("Which door do you want to open? \n")
 if door == "blue":
   print("You open the door and found a box filled with crocodiles 🐊🐊🐊\nGame over! �")
   time.sleep(1)
   play_again = input("Do you want to play again?").lower()
   while play_again != "yes" and play_again != "no":
     print("Sorry, Inavlid choice! 🤷‍♂️🤷‍♂")
     time.sleep(1)
     play_again = input("Do you want to play again?").lower()
   if play_again == "yes":
     pirate_island_puzzle()
   elif play_again == "no":
     print("Good bye!")
 elif door == "red":
   print("Good, now you entered a room.")
   red_door()


def red_door():
  box = input("You found three boxes: 🎁 white, 🎁 black, 🎁 green �\nChoose one of them: \n")
  while box != "white" and box != "black" and box != "green":
     print("Sorry, Inavlid choice! 🤷‍♂️🤷‍♂️🤷‍")
     time.sleep(1)
     box = input("You found three boxes: 🎁 white, 🎁 black, 🎁 green �\nChoose one of them: \n")
  if box == "white":
     print("Oops! You opened a box filled with snakes 🐍🐍🐍\nGame over!")
     time.sleep(1)
     play_again = input("Do you want to play again?").lower()
     while play_again != "yes" and play_again != "no":
       print("Sorry, Inavlid choice! 🤷‍♂️🤷‍♂")
       time.sleep(1)
       play_again = input("Do you want to play again?").lower()
     if play_again == "yes":
       red_door()
     elif play_again == "no":
       print("Good bye!")
  elif box == "black":
     print("Oops! You opened a box filled with spiders 🕷️🕷️🕷️\nGame over!")
     time.sleep(1)
     play_again = input("Do you want to play again?").lower()
     while play_again != "yes" and play_again != "no":
       print("Sorry, Inavlid choice! 🤷‍♂️🤷‍♂")
       time.sleep(1)
       play_again = input("Do you want to play again?").lower()
     if play_again == "yes":
       red_door()
     elif play_again == "no":
       print("Good bye!")
  elif box == "green":
     print("Congratulations! You found the treasure! 💰💰💰")
     time.sleep(1)
     play_again = input("Do you want to play again?").lower()
     while play_again != "yes" and play_again != "no":
       print("Sorry, Inavlid choice! 🤷‍♂️🤷‍♂")
       time.sleep(1)
       play_again = input("Do you want to play again?").lower()
     if play_again == "yes":
       pirate_island_puzzle()
     elif play_again == "no":
       print("Good bye!")

pirate_island_puzzle()
  
  