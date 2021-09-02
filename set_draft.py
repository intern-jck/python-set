# Set Game
# Justin Kirk
# 2021

# Explain game some more here

import tkinter as tk
import glob
import random

set_root = tk.Tk()
set_root.title("Set Game")
set_root.geometry("800x500")
set_root.config(bg="grey")

GAME_ROW = 3
GAME_COL = 5
MAX_CARDS = 81


# button_image = tk.PhotoImage(file=".\SetCards\Set Card_0.png")

# Get path names for card images
card_image_paths = glob.glob("SetCards\*.png")
card_images = []
# Save them to access later
for i in range(MAX_CARDS):
    card_image = tk.PhotoImage(file=card_image_paths[i])
    card_images.append(card_image)


# Each card can be represented by its ternary value
def ternary(n):
    # Simple case
    if n == 0:
        return "0000"
    # Build string
    num = ""
    while n:
        n, r = divmod(n, 3)
        num = num + (str(r))
    # Reverse String
    num = num[::-1]
    # Padd with leading zeros if needed
    if len(num) == 1:
        return "000" + num
    elif len(num) == 2:
        return "00" + num
    elif len(num) == 3:
        return "0" + num
    elif len(num) == 4:
        return "" + num


card_values = [[0, 0, 0, 0] for i in range(MAX_CARDS)]
# Fill in all the values for cards
for i in range(MAX_CARDS):
    # print(ternary(i))
    for j in range(len(card_values[i])):
        card_values[i][j] = ternary(i)[j]

# Used to check if card has been drawn
card_drawn = [False for i in range(MAX_CARDS)]
card_selected = [False for i in range(MAX_CARDS)]
# Used to check if card can be placed on table
card_grid = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]


card_set = [[] for i in range(3)]


def card_click(num):
    card_selected[num] = not card_selected[num]


def new_game():
    print("New Game")
    # Layout cards
    for i in range(GAME_ROW):
        for j in range(GAME_COL - 1):
            card_num = random.randrange(MAX_CARDS)
            new_card = tk.Button(
                set_root,
                image=card_images[card_num],
                bg="black",
                activebackground="red",
            )
            new_card.place(x=40 + j * 100, y=40 + i * 140)


def clear_table():
    print("Clear Table")


def draw_three():
    print("Draw Three More")


new_game_button = tk.Button(set_root, text="New Game", command=new_game)
clear_table_button = tk.Button(set_root, text="Clear", command=clear_table)
draw_three_button = tk.Button(set_root, text="Draw 3", command=draw_three)
new_game_button.place(x=700, y=200)
clear_table_button.place(x=700, y=250)
draw_three_button.place(x=700, y=300)

set_root.mainloop()
