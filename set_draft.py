# Set Game
# Justin Kirk
# 2021

# Explain game some more here

import tkinter as tk
import glob
import random
from functools import partial
import re

# Tkinter setup
set_root = tk.Tk()
set_root.title("Set Game")
set_root.geometry("800x500")
set_root.config(bg="grey")

# Make a grid of 3 rows by 5 cols to place cards
GAME_ROW = 3
GAME_COL = 5
# 81 Total cards in the deck
MAX_CARDS = 81
# Used to check if card can be placed on table
###NIU at the moment
card_grid = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]


# Use images of each card for buttons
# Get path names for card images
card_image_paths = glob.glob("SetCards\*.png")
card_image_paths = sorted(card_image_paths, key=lambda n: int(re.findall(r"\d+", n)[0]))

# Save them to access later
card_images = []
for i in range(MAX_CARDS):
    card_image = tk.PhotoImage(file=card_image_paths[i])
    card_images.append(card_image)


# Each card can be represented by its ternary value
# This makes a ternary representation for each card
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


# Save the values for each card
card_values = [[0, 0, 0, 0] for i in range(MAX_CARDS)]
# Fill in all the values for cards
for i in range(MAX_CARDS):
    for j in range(len(card_values[i])):
        card_values[i][j] = int(ternary(i)[j])

# Keep track of cards drawn and selected
card_drawn = [False for i in range(MAX_CARDS)]
card_selected = [False for i in range(MAX_CARDS)]

card_set = []


card_buttons = [0 for i in range(MAX_CARDS)]


def new_game():
    print("New Game")
    card_deck = [i for i in range(MAX_CARDS)]

    # Clear everything
    # clear_table()
    for i in range(len(card_set)):
        card_set.pop(i)

    # for i in range(MAX_CARDS):
    #     card_drawn[i] = False

    # Layout cards
    for i in range(MAX_CARDS):
        card = tk.Button(
            set_root,
            image=card_images[i],
            bg="black",
            command=partial(card_click, i),
        )
        card_buttons[i] = card

    for i in range(3):
        for j in range(4):

            # card_num = random.randrange(MAX_CARDS)
            card_num = random.randrange(len(card_deck))
            card_placed = card_deck[card_num]

            print(card_num, " ", end="")

            if card_drawn[card_placed] == False:
                card_buttons[card_placed].place(x=40 + j * 100, y=40 + i * 140)
                card_drawn[card_placed] = True
                index = card_deck.index(card_placed)
                card_deck.pop(index)
        print()


def clear_table():

    print("Clear Table")
    for i in range(len(card_set)):
        card_set.pop(i)

    for i in range(MAX_CARDS):
        card_drawn[i] = False


def card_click(num):

    card_selected[num] = not card_selected[num]

    if card_selected[num] == True:

        if len(card_set) < 3:
            card_set.append(num)
            card_buttons[num].config(bg="red")
            print(card_set)
            # print("{}: {}".format(num, card_values[num]))

    elif card_selected[num] == False:
        if num in card_set:
            index = card_set.index(num)
            card_set.pop(index)
            print(len(card_set))
            card_buttons[num].config(bg="black")
        print(card_set)


def draw_three():
    print("Draw Three More")
    for i in range(3):
        card_buttons[i].place(x=440, y=40 + i * 140)


def check_set():
    if len(card_set) == 3:
        card_1 = card_values[card_set[0]]
        card_2 = card_values[card_set[1]]
        card_3 = card_values[card_set[2]]

        if (
            (card_1[0] == card_2[0] == card_3[0] or card_1[0] != card_2[0] != card_3[0])
            and (
                card_1[1] == card_2[1] == card_3[1]
                or card_1[1] != card_2[1] != card_3[1]
            )
            and (
                card_1[2] == card_2[2] == card_3[2]
                or card_1[2] != card_2[2] != card_3[2]
            )
            and (
                card_1[3] == card_2[3] == card_3[3]
                or card_1[3] != card_2[3] != card_3[3]
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
