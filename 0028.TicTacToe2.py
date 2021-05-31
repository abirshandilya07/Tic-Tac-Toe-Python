board=["1","2","3","4","5","6","7","8","9"]

def updated_board():
        ret_str = " " + board[0]+ " | " + board[1] + " | " + board[2] + " \n"
        ret_str += "---|---|---\n"
        ret_str += " " + board[3]+ " | " + board[4] + " | " + board[5] + " \n"
        ret_str += "---|---|---\n"
        ret_str += " " + board[6]+ " | " + board[7] + " | " + board[8] + " \n"
        return ret_str
        
def put_x_o(x_o):
        while True:
            block_no_str=input("Block no : ")
            if block_no_str.isnumeric()==False:
                print("Invalid Input. Block no should be numeric only. Enter block no again")
                continue
            
            block_no=int(block_no_str)
            
            if block_no<1 or block_no>9:
                print("Invalid Input. Block no should b1 between 1 to 9. Enter block no again")
            elif board[block_no-1]=="X" or board[block_no-1]=="O":
                print("This block is already occupied, Enter block no again")
            else:                 
                board[block_no-1]=x_o
                break
def next_move(x_o):

    move_made=False

    #priority 1 can we win

    if move_made==False:
        for i in range(9):
            if board[i]!="X" and board[i]!="O": #empty check
                board[i]=x_o
                if check_win(x_o)=="win":
                    move_made=True #we won
                    break
                else:
                    board[i]=str(i+1)
            
    #priority 2 can we block

    if move_made==False:
        if x_o=="X":
            opp_x_o="O"
        else:
            opp_x_o="X"
            
        for i in range(9):
            if board[i]!="X" and board[i]!="O": #empty check
                board[i]=opp_x_o
                if check_win(opp_x_o)=="win":
                    board[i]=x_o
                    move_made=True #we blocked successfully
                    break
                else:
                    board[i]=str(i+1)

    #priority 3 is center empty
    if move_made==False:
        if board[4]!= "X" and board[4]!="O": #empty check
            board[4]=x_o
            move_made=True #Placed at center successfully

    #priority 4 is any corner empty
    if move_made==False:
        for i in [0,2,6,8]:
            if board[i]!= "X" and board[i]!="O": #empty check
                board[i]=x_o
                move_made=True #Placed at corner successfully
                break

    #priority 5 is any edge empty
    if move_made==False:
        for i in [1,3,5,7]:
            if board[i]!= "X" and board[i]!="O": #empty check
                board[i]=x_o
                move_made=True #Placed at edge successfully
                break
            
def check_win(x_o):
        #row win check
        if board[0]==x_o and board[1]==x_o and board[2]==x_o:
            return "win"
        elif board[3]==x_o and board[4]==x_o and board[5]==x_o:
            return "win"
        elif board[6]==x_o and board[7]==x_o and board[8]==x_o:
            return "win"
        #column win check
        elif board[0]==x_o and board[3]==x_o and board[6]==x_o:
            return "win"
        elif board[1]==x_o and board[4]==x_o and board[7]==x_o:
            return "win"
        elif board[2]==x_o and board[5]==x_o and board[8]==x_o:
            return "win"
        #diagonal win check
        elif board[0]==x_o and board[4]==x_o and board[8]==x_o:
            return "win"
        elif board[2]==x_o and board[4]==x_o and board[6]==x_o:
            return "win"
        else:
            return "game on"


print("Hello")
print("I am Jarvis2")
ans=input("Do you want play with Jarvis2 or any human?\nType j for Jarvis2 and any other key for human: ")
if ans.upper()!="J":
    player1=input("What is the name of first player?\n")
    player2=input("What is the name of second player?\n")

    game_over=False
        
    print(updated_board())

    for i in range(1,10):
        if i%2!=0:
            print(player1+" its your turn. Put X in any one of the vacant blocks by clicking a number from 1 to 9")
            put_x_o("X")
            print(updated_board())
            if check_win("X")=="win":
                print("Congratulations !!!, " + player1+" you won and you are khiladi. Sorry " + player2 + " you lost and you are anadi")
                game_over=True
                break      
        else:
            print(player2+" its your turn. Put O in any one of the vacant blocks by clicking a number from 1 to 9")
            put_x_o("O")         
            print(updated_board())
            if check_win("O")=="win":
                print("Congratulations !!!, " + player2+" you won and you are khiladi. Sorry " + player1 + " you lost and you are anadi")
                game_over=True
                break
            
    if game_over==False:
        print("Game over. No move left. It's a tie. No one won.")
        
else:
    name=input("What is your name?\n")
    player_no=input("Do you want to play first? Type Y for yes any other key for no: ")
    
    if player_no.upper()=="Y":
        print(name,"is playing first with X.")
        print("Jarvis2 is playing second with O.")
        player1=name
        player2="Jarvis2"
    else :
        print("Jarvis2 is playing first with X.")
        print(name,"is playing second with O.")
        player1="Jarvis2"
        player2=name
    
    game_over=False
        
    print(updated_board())

    for i in range(1,10):
        if i%2!=0:
            if player1!= "Jarvis2":
                print(player1+" its your turn. Put X in any one of the vacant blocks by clicking a number from 1 to 9")
                put_x_o("X")
                print(updated_board())
                if check_win("X")=="win":
                    print("Congratulations !!!, " + player1+" you won and you are khiladi. Sorry " + player2 + " you lost and you are anadi")
                    game_over=True
                    break      
            else:
                print("Jarvis2 making it's move")
                next_move("X")
                print("Jarvis2 made the move")
                print(updated_board())
                if check_win("X")=="win":
                    print("Congratulations !!!, " + player1+" you won and you are khiladi. Sorry " + player2 + " you lost and you are anadi")
                    game_over=True
                    break      
        else:
            if player2!= "Jarvis2":
                print(player2+" its your turn. Put O in any one of the vacant blocks by clicking a number from 1 to 9")
                put_x_o("O")         
                print(updated_board())
                if check_win("O")=="win":
                    print("Congratulations !!!, " + player2+" you won and you are khiladi. Sorry " + player1 + " you lost and you are anadi")
                    game_over=True
                    break
            else:
                print("Jarvis2 making it's move")
                next_move("O")
                print("Jarvis2 made the move")
                print(updated_board())
                if check_win("O")=="win":
                    print("Congratulations !!!, " + player2+" you won and you are khiladi. Sorry " + player1 + " you lost and you are anadi")
                    game_over=True
                    break
            
    if game_over==False:
        print("Game over. No move left. It's a tie. No one won.")
