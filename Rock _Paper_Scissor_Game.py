import random,sys
print('\n \t\t\t\t ******Rock,Paper and Scissors*******')
# track win,loss,tie
win=0
loss=0
tie=0

# Loop the main game

while True:
    print(f"win: {win}\nloss: {loss}\ntie: {tie}")

    print ("""Enter your move':
            r=Rock,
            p=Paper,
            s=Scissor,
            q=Quit""")
    User_move=input("\n Type one of r,p,s or q:")
    if User_move=='q':
        sys.exit()     # Quit the program

    import numpy as np
# Display what the computer choice
    random_number=random.randint(1,3)

    # Let computer chose its move
    if random_number==1:
        computer_move='r'
        print('Rock')

    elif random_number==2:
        computer_move='p'
        print('Paper')

    elif random_number==3:
        computer_move='s'
        print('Scissor')


        if User_move == computer_move:
            print('It is a Tie:!')
            tie+=1

        elif User_move =='r' and computer_move =='s':
            win += 1
            print('you wins!')

        elif User_move == 's' and computer_move == 'r':
            loss += 1
            print('you lose!')

        elif User_move =='s' and computer_move =='p':
            win += 1
            print('you wins!')

        elif User_move == 'p' and computer_move == 's':
            loss += 1
            print('you lose!')

        elif User_move == 'r' and computer_move == 's':
            win += 1
            print('you wins!')

        elif User_move =='r' and computer_move =='s':
            win += 1
            print('you wins!')

        elif User_move == 'p' and computer_move == 'r':
            win += 1
            print('you wins!')

        elif User_move == 'r' and computer_move == 'p':
            loss += 1
            print('you lose!')
