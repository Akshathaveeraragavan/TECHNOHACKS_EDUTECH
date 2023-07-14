#This is the popular ROCK,PAPER,SCISSORS GAME application.Here,its played between the user and the computer.
import random
while True:
    l1 = ["Rock", "Paper", "Scissors"]  # This is a list
    choice=int(input('Press 1 for single player and 2 for Multiplayer:'))
    if choice==1:
        name = input("Enter your name to start the game!")
        print("Welcome,", name)
        result = random.choice(l1)
        print("Lets start the game...Gear up!!!")
        print(name,'Vs Computer')
        user = input("Enter your option:Rock,Paper or Scissors???")
        print("COMPUTER'S CHOICE-", result)
        print("YOUR CHOICE-", user)
        if (result == user):
            print("Oh,its a draw!!")
        elif (result == "Rock" and user == "Paper") or (result == 'Rock' and user == 'paper'):
            print("Sorry.You lose!")
        elif (result == "Paper" and user == "Rock") or (result == 'Paper' and user == 'rock'):
            print("Hurray!You win!!")
        elif (result == "Paper" and user == "Scissors") or (result == 'Paper' and user == 'scissors'):
            print("Hurray!You win!!")
        elif (result == "Scissors" and user == "Paper") or (result == 'Scissors' and user == 'paper'):
            print("Sorry.You lose!")
        elif (result == "Scissors" and user == "Rock") or (result == 'Scissors' and user == 'rock'):
            print("Hurray!You win!!")
        elif (result == "Rock" and user == "Scissors") or (result == 'Rock' and user == 'scissors'):
            print("Sorry.You lose!")
        else:
            print("Invalid entry.Please try again")
        play_again = input('Would you like to play again?\nY/N')
        if play_again=='Y' or play_again=='y':
            continue
        else:
            print("Thank you for using our application.\nCome back again ",name,"!!!")
            break
    elif choice==2:
        user1=input('Enter player 1 name to get started:')
        user2 =input('Enter player 2 name to get started:')
        print("Lets start the game...Gear up!!!")
        print(user1,'Vs',user2)
        player1 = input("Enter your option:Rock,Paper or Scissors???"+user1)
        player2 = input("Enter your option:Rock,Paper or Scissors???"+user2)
        print(user1,"-", player1)
        print(user2,"-", player2)
        if ( player1== player2):
            print("Oh,its a draw!!")
        elif (player1 == "Rock" and player2 == "Paper") or (player1 == 'rock' and player2 == 'paper')or (player1== 'Rock' and player2 == 'paper')or (player1== 'rock' and player2 == 'Paper'):
            print("Sorry.You lose!")
        elif (player1== "Paper" and player2== "Rock") or (player1== 'paper' and player2== 'rock')or (player1== 'Paper' and player2 == 'rock')or (player1== 'paper' and player2 == 'Rock'):
            print("Hurray!You win!!")
        elif (player1 == "Paper" and player2 == "Scissors") or (player1== 'paper' and player2 == 'scissors')or (player1== 'Paper' and player2 == 'scissors')or (player1== 'paper' and player2 == 'Scissors'):
            print("Hurray!You win!!")
        elif (player1 == "Scissors" and player2 == "Paper") or (player1 == 'scissors' and player2 == 'paper')or (player1 == 'Scissors' and player2 == 'paper')or (player1== 'scissors' and player2 == 'Paper'):
            print("Sorry.You lose!")
        elif (player1 == "Scissors" and player2 == "Rock") or (player1 == 'scissors' and player2 == 'rock')or (player1 == 'Scissors' and player2 == 'rock')or (player1== 'scissors' and player2 == 'Rock'):
            print("Hurray!You win!!")
        elif (player1 == "Rock" and player2 == "Scissors") or (player1 == 'rock' and player2 == 'scissors')or (player1 == 'Rock' and player2 == 'scissors')or (player1== 'rock' and player2 == 'Scissors'):
            print("Sorry.You lose!")
        else:
            print("Invalid entry.Please try again")
        play_again = input('Would you like to play again?\nY/N')
        if play_again == 'Y' or play_again == 'y':
            continue
        else:
            print("Thank you for using our application.\nCome back again ", name, "!!!")
            break
    else:
        print('Oops,that was an invalid choice . Please Try again!!!')


