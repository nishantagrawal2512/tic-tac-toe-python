def printgrid(t):
        print(f'    |   |    ')
        print(f' {t[7]}  | {t[8]} | {t[9]}  ')
        print(f'____|___|____')
        print(f'    |   |    ')
        print(f' {t[4]}  | {t[5]} | {t[6]}  ')
        print(f'____|___|____')
        print(f'    |   |    ')
        print(f' {t[1]}  | {t[2]} | {t[3]}  ')
        print(f'    |   |    ')

def checkvictory():
    global victoryLetter
    global victoryPlayer
    if t[1]==t[2]==t[3] and t[1] in ['X','O']:
        victoryLetter=t[1]
        return True
    elif t[4]==t[5]==t[6] and t[4] in ['X','O']:
        victoryLetter=t[4]
        return True
    elif t[7]==t[8]==t[9] and t[7] in ['X','O']:
        victoryLetter=t[7]
        return True
    elif t[7]==t[4]==t[1] and t[7] in ['X','O']:
        victoryLetter=t[7]
        return True
    elif t[8]==t[5]==t[2] and t[8] in ['X','O']:
        victoryLetter=t[8]
        return True
    elif t[9]==t[6]==t[3] and t[9] in ['X','O']:
        victoryLetter=t[9]
        return True
    elif t[7]==t[5]==t[3] and t[7] in ['X','O']:
        victoryLetter=t[7]
        return True
    elif t[9]==t[5]==t[1] and t[9] in ['X','O']:
        victoryLetter=t[9]
        return True
    else:
        return False

def play(p):

    def togglePlayer(oldplayer):
        if oldplayer==1:
            newplayer=2
        else:
            newplayer=1
        return newplayer

    print(f'Current player is Player: {p}')
    currentTurnValid=False
    while currentTurnValid==False:
        currentTurn=input(f'Enter your turn Player{p}: ')
        if currentTurn==None or currentTurn.isspace() or currentTurn=='':
            print('Please choose correct number')
        elif int(currentTurn) not in possiblePlay:
            print('Please choose correct number')
        else:
            currentTurnValid=True

    t[int(currentTurn)]=choices.get(p)
    possiblePlay.discard(int(currentTurn))
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    printgrid(t)
    global gameOver
    gameOver=checkvictory()
    p=togglePlayer(p)
    return(p)


if __name__ == "__main__":
    
    t=['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    b=['#','1','2','3','4','5','6','7','8','9']
    possiblePlay={1,2,3,4,5,6,7,8,9}
    playbool=False
    p1choicebool=False
    setup=False
    currentPlayer=1
    totalTurn=0
    maxTurn=9
    gameOver=False
    victoryLetter=None
    victoryPlayer=None

    while playbool==False:
        playflag=input('\n\n\n\n\nDo you want to play TIC TAC TOE? (y/n): ')
        playbool=playflag[0].lower()=='y'
        if not playbool:
            break


    while p1choicebool==False and playbool==True and setup==False:
        p1choice=input('\n\nPlayer 1, do you want to be X or O: ')
        options=['X','O']
        if p1choice not in options:
            print('Please choose correct option')
            p1choicebool=False
        else:
            p1choicebool=True
            # print('   |  |   \n___|__|___\n   |  |   \n___|__|___\n   |  |   \n   |  |   ')
            printgrid(b)
            p1=p1choice
            global choices
            if p1=='X':
                choices={1:'X',2:'O'}
            else:
                choices={1:'O',2:'X'}
            setup=True
            print('The game is now set up!\n\n')
            print(f'Player 1 is {choices.get(1)} and Player 2 is {choices.get(2)}\n\n')

    while True:
        if totalTurn>=maxTurn or gameOver or not playbool:
            break
        else:
            currentPlayer=play(currentPlayer)
            totalTurn+=1
            # print(f'Total number of turns = {totalTurn}')
            # print(f'Valid choices remaining are {possiblePlay}')

    if victoryLetter!=None or totalTurn==maxTurn:
        print('\n\nThe game has ended!')
        if totalTurn==maxTurn:
            print('This game is a tie!')
        else:
            print('TIC TAC TOE -- THREE IN A ROW!!')
            print(f'Player {list(choices.keys())[list(choices.values()).index(victoryLetter)]} ({victoryLetter}) has won the game')

