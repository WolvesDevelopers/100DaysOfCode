import random as rd
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock,paper,scissors]
computer_option = rd.randint(0,2)

prompt = "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"
player_option = int(input(prompt))

#conditional alternative.

if player_option >= 3 or player_option < 0: 
  print("You typed an invalid number, you lose!") 

#Draw
elif(player_option == computer_option):
  print(options[player_option])
  print("Computer chose:")
  print(options[computer_option])
  print("Draw.")

#Player Win
elif(player_option == 0 and computer_option == 2):
  print(options[player_option])
  print("Computer chose:")
  print(options[computer_option])
  print("You Win.")

elif(player_option > computer_option):
  print(options[player_option])
  print("Computer chose:")
  print(options[computer_option])
  print("You Win.")


#Computer Win

elif(computer_option == 0 and player_option == 2):
  print(options[player_option])
  print("Computer chose:")
  print(options[computer_option])
  print("You Lose.")


elif(computer_option > player_option):
  print(options[player_option])
  print("Computer chose:")
  print(options[computer_option])
  print("You Lose.")


