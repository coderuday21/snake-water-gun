def play(c,h):
    win=''
    if c=='s':
        if h=='w':
            win='c'
        elif h=='g':
            win='h'
        else:
            win='t'
    elif c=='w':
        if h=='w':
            win='t'
        elif h=='g':
            win='c'
        else:
            win='h'
    elif c=='g':
        if h=='w':
            win='h'
        elif h=='s':
            win='c'
        else:
            win='t'
    return win


import random
choice=True
game_played=0
make_choice=['s','w','g']
abrre_to_full={'s':'Snake','w':'Water','g':'Gun'}
score_board=[]
print("Welcome to Snake,Water,Gun Game")
print("Press S for Snake, W for Water and G for Gun")

while choice:
    while game_played<10:
        print(f'{10-game_played} to go')
        print(f"Computer Scored:{score_board.count('c')} Human Scored:{score_board.count('h')}")
        computer=random.choice(make_choice)
        human=input("Choose Snake(s), Water(w), Gun(g)")
        score_board.append(play(computer,human))
        if score_board[game_played]=='c':
            print(f"Computer chose {abrre_to_full[computer]} and human chose {abrre_to_full[human]}")
            print("Computer Wins")
        elif score_board[game_played]=='h':
            print(f"Computer chose {abrre_to_full[computer]} and human chose {abrre_to_full[human]}")
            print("Human Wins")
        else:
            print(f"Computer chose {abrre_to_full[computer]} and human chose {abrre_to_full[human]} also")
            print("Match Draw")
        game_played+=1
    else:
        print(score_board)
        if score_board.count('c')>score_board.count('h'):
            print("Computer Wins The Game")
        elif score_board.count('c')<score_board.count('h'):
            print("Human Wins The Game")
        else:
            print("Match Tied")
        choice=input("Do you want to continue:")
        if choice=='y' or choice=="yes":
            choice=True
            game_played=0
            score_board.clear()
        else:
            choice=False
else:
    print("Thanks for playing, Have a good day")
