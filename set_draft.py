# Set Game
# Justin Kirk
# 2021

# Explain game some more here

import tkinter as tk
import glob
import random
from functools import partial
import re

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
card_image_paths = sorted(card_image_paths, key=lambda n: int(re.findall(r"\d+", n)[0]))

for path in card_image_paths:
    print(path)

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
        card_values[i][j] = int(ternary(i)[j])

    # print("{}: {}".format(i, card_values[i]))

# Used to check if card has been drawn
card_drawn = [False for i in range(MAX_CARDS)]
card_selected = [False for i in range(MAX_CARDS)]

# Used to check if card can be placed on table
card_grid = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]


# card_set = [[] for i in range(3)]
card_set = []


def card_click(num):

    card_selected[num] = not card_selected[num]

    if card_selected[num] == True:
        # card_set.append(num)
        card_deck[num].config(bg="red")
        print("{}: {}".format(num, card_values[num]))
    elif card_selected[num] == False:
        # index = card_set.index(num)
        # card_set.pop(index)
        card_deck[num].config(bg="black")


card_deck = [0 for i in range(MAX_CARDS)]


def new_game():
    print("New Game")

    # Clear everything
    # clear_table()
    for i in range(len(card_set)):
        card_set.pop(i)

    for i in range(MAX_CARDS):
        card_drawn[i] = False
    # Layout cards
    for i in range(MAX_CARDS):
        card = tk.Button(
            set_root,
            image=card_images[i],
            bg="black",
            activebackground="red",
            command=partial(card_click, i),
        )
        card_deck[i] = card

    for i in range(GAME_ROW):
        for j in range(GAME_COL - 1):
            card_num = random.randrange(MAX_CARDS)

            if card_drawn[card_num] == False:
                card_deck[card_num].place(x=40 + j * 100, y=40 + i * 140)
                card_drawn[card_num] = True


def clear_table():

    print("Clear Table")
    for i in range(len(card_set)):
        card_set.pop(i)

    for i in range(MAX_CARDS):
        card_drawn[i] = False


def draw_three():
    print("Draw Three More")
    for i in range(3):
        card_deck[i].place(x=440, y=40 + i * 140)


def check_set():
    if len(card_set) == 3:
        for card in card_set:
            print(card)
        if (
            (
                card_set[0][0] == card_set[1][0] == card_set[2][0]
                or card_set[0][0] != card_set[1][0] != card_set[2][0]
            )
            and (
                card_set[0][1] == card_set[1][1] == card_set[2][1]
                or card_set[0][1] != card_set[1][1] != card_set[2][1]
            )
            and (
                card_set[0][2] == card_set[1][2] == card_set[2][2]
                or card_set[0][2] != card_set[1][2] != card_set[2][2]
            )
            and (
                card_set[0][3] == card_set[1][3] == card_set[2][3]
                or card_set[0][3] != card_set[1][3] != card_set[2][3]
            )
        ):
            print("Set Found!")
        else:
            print("NOT A SET!!!")

    else:
        print("Need A Full Set!")
        return


new_game_button = tk.Button(set_root, text="New Game", command=new_game)
clear_table_button = tk.Button(set_root, text="Clear", command=clear_table)
draw_three_button = tk.Button(set_root, text="Draw 3", command=draw_three)
check_set_button = tk.Button(set_root, text="Check Set", command=check_set)
new_game_button.place(x=700, y=100)
clear_table_button.place(x=700, y=150)
draw_three_button.place(x=700, y=200)
check_set_button.place(x=700, y=250)

set_root.mainloop()
