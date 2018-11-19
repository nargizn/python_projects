from tkinter import *
class Cell:
    def __init__(self, number, window):
        self.symbol = ' '
        self.number = number
        self.canvas = Canvas(window, height=100, width=100,
                             bd=2, highlightbackground = "red")
        self.canvas.grid(row=(number-1)//3+1, column=(number-1)%3+1)

    def clear(self):
        self.canvas.delete(ALL)
        self.symbol = ' '
