from tkinter import *
from cell import *
import random
import os.path
from tkinter import messagebox

def write_score():
    file = open("score.txt", "w")
    file.write(str(computer_score))
    file.write("\n")
    file.write(str(player_score))
    file.close()

def read_score():
    if not os.path.exists("score.txt"):
        return 0, 0
    file = open("score.txt", "r")
    c = int(file.readline())
    p = int(file.readline())
    return c, p

def has_won(symbol):
    if board[1].symbol+board[2].symbol+board[3].symbol == symbol*3:
        return True
    if board[4].symbol+board[5].symbol+board[6].symbol == symbol*3:
        return True
    if board[7].symbol+board[8].symbol+board[9].symbol == symbol*3:
        return True
    if board[1].symbol+board[4].symbol+board[7].symbol == symbol*3:
        return True
    if board[2].symbol+board[5].symbol+board[8].symbol == symbol*3:
        return True
    if board[3].symbol+board[6].symbol+board[9].symbol == symbol*3:
        return True
    if board[1].symbol+board[5].symbol+board[9].symbol == symbol*3:
        return True
    if board[3].symbol+board[5].symbol+board[7].symbol == symbol*3:
        return True
    return False

def ai():
    move = 0
    for position in range(1,10):
        if board[position].symbol==" ":
            board[position].symbol = computer
            if has_won(computer):
                move = position
                break
            else:
                board[position].symbol = " "
    if move == 0:
        for position in range(1,10):
            if board[position].symbol==" ":
                board[position].symbol = player
                if has_won(player):
                    move = position
                    break
                else:
                    board[position].symbol = " "

    if move==0:
        free_positions = []
        for position in [1, 3, 7, 9]:
            if board[position].symbol==" ":
                free_positions.append(position)
        if len(free_positions) > 0:
            move = random.choice(free_positions)

    if move==0 and board[5].symbol==" ":
        move = 5

    if move==0:            
        free_positions = []
        for position in [2, 4, 6, 8]:
            if board[position].symbol==" ":
                free_positions.append(position)
        if len(free_positions) > 0:
            move = random.choice(free_positions)

    return move
    

def draw(number, symbol):
    board[number].canvas.create_text(50, 50, text=symbol, font="Arial, 50")
    board[number].symbol = symbol

def click(event, obj):
    global turns, player_score, computer_score
    if event != -1:
        if obj.symbol != ' ':
            return
        draw(obj.number, player)
        turns += 1
        if has_won(player):
            player_score += 1
            messagebox.showinfo("Победа!", "Молодец ты победил :) !!!")
            restart()
            return

    if turns == 9:
        messagebox.showinfo("Ничья!", "Хороший результат! Ничья :) !!!")
        restart()
        return
        
    computer_move = ai()
    draw(computer_move, computer)
    turns += 1
    if has_won(computer):
        computer_score += 1
        messagebox.showinfo("Поражение!", "Извини, ты проиграл :( !!!")
        restart()
        return
        
    if turns == 9:
        messagebox.showinfo("Ничья!", "Хороший результат! Ничья :) !!!")
        restart()
        return



def restart():
    score_label.config(text=str(computer_score)+ " : "+str(player_score))
    write_score()
    answer = messagebox.askquestion("Кем будешь играть?", "Будешь ли играть крестиком?")

    for i in range(1, 10):
        board[i].clear()
    global player
    global computer
    global turns

    turns = 0
    
    if answer == 'no':
        player = 'O'
        computer = 'X'
        click(-1, -1)
    else:
        player = 'X'
        computer = 'O'
        
    
def leave_game():
    window.destroy()
    
window = Tk()

# добавление меню
menubar = Menu(window)
gamemenu = Menu(menubar, tearoff=0)
gamemenu.add_command(label="Restart", command = restart)
gamemenu.add_command(label="Exit", command = leave_game)

menubar.add_cascade(label="Game", menu=gamemenu)
window.config(menu=menubar)

score_label = Label(window, text="0 : 0")
score_label.grid(row=0, column=2)

player = 'X'
computer = 'O'

computer_score, player_score = read_score()

turns = 0
board = [' ']

for i in range(1, 10):
    cell = Cell(i, window)
    cell.canvas.bind("<Button-1>", lambda event, obj=cell: click(event, obj))
    board.append(cell)



restart()

window.mainloop()
