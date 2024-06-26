import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

class FlipCardGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Flip Card Game")
        
        self.cards = ['hackclub', 'github', 'hackclub', 'github']
        random.shuffle(self.cards)
        
        self.images = {
            'hackclub': ImageTk.PhotoImage(Image.open("hackclub_logo.png")),
            'github': ImageTk.PhotoImage(Image.open("github_logo.png")),
            'back': ImageTk.PhotoImage(Image.open("card_back.png"))
        }
        
        self.buttons = []
        self.flipped = []
        
        for i in range(4):
            button = tk.Button(self.root, image=self.images['back'], command=lambda i=i: self.flip_card(i))
            button.grid(row=i//2, column=i%2)
            self.buttons.append(button)
    
    def flip_card(self, index):
        if len(self.flipped) < 2:
            self.buttons[index].config(image=self.images[self.cards[index]])
            self.flipped.append(index)
        
        if len(self.flipped) == 2:
            self.root.after(1000, self.check_match)
    
    def check_match(self):
        first, second = self.flipped
        if self.cards[first] == self.cards[second]:
            messagebox.showinfo("Match!", "You found a match!")
            self.buttons[first].config(state="disabled")
            self.buttons[second].config(state="disabled")
        else:
            self.buttons[first].config(image=self.images['back'])
            self.buttons[second].config(image=self.images['back'])
        
        self.flipped = []

if __name__ == "__main__":
    root = tk.Tk()
    game = FlipCardGame(root)
    root.mainloop()
