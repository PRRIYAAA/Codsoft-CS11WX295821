def play():
    import random 
    count_computer=0
    count_user=0
    lis=['rock','paper','scissors']
    user_input=input('Enter the input:')
    if user_input in lis:
        print('ok continue ')
    else:
        print('Invalid input')

    computer_selection=random.choice(lis)
    if computer_selection==user_input:
        print("It's a tie!")
        
    elif computer_selection=='rock' and user_input=='scissors':
        print("Computer wins!")
        count_computer+=1
        
    elif computer_selection=='rock' and  user_input=='paper':
        print("User wins!")
        count_user+=1
        
    elif computer_selection=='paper' and user_input=='scissor':
        print("User wins!")
        count_user+=1
        
    elif computer_selection=='paper' and user_input=='rock':
        print("Computer wins!")
        count_computer+=1

    elif computer_selection=='scissors' and user_input=='paper':
        print("Computer wins!")
        count_computer+=1
        
    elif computer_selection=='scissors' and user_input=='rock':
        print("User wins!")
        count_user+=1

    if count_computer>count_user:
        print("Computer wins the game!"+ 'points:'+ count_computer)

        
    else:
        print("User wins the game!"+'points:'+ count_user)

start=play()

play_input = input("Do you want to play again? (yes/no): ").lower()
if 'yes':
    play()
else:
    print("Thanks for playing!")
            



