import random


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

#Write your code below this line 👇



valid_choices = {
    1: rock,
    2: paper,
    3: scissors,
    'rock': rock,
    'paper': paper,
    'scissors': scissors
}

matchups = {
    rock: scissors,
    paper: rock,
    scissors: paper
}

def get_user_input():
    user_choice = input("What do you choose? Type 1 for Rock, 2 for Paper or 3 for Scissors.\n")
    if user_choice.isdigit() and int(user_choice) in valid_choices:     
        return valid_choices[int(user_choice)]
    
    if user_choice.lower() in valid_choices:
        return valid_choices[user_choice.lower()]
        
    print("Invalid choice")
    return get_user_input()

def get_computer_choice():
    return valid_choices[random.randint(1, 3)]

def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a draw"
    
    if matchups[user_choice] == computer_choice:
        return "You win!"
    
    return "You lose!"


user_choice = get_user_input()
computer_choice = get_computer_choice()

print(f"You chose:\n{user_choice}")
print(f"Computer chose:\n{computer_choice}")

print(get_winner(user_choice, computer_choice))