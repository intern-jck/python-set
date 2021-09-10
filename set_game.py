import tkinter as tk
import tkinter.font as tkfont
from functools import partial
import random
import re
import glob

# Set Game


class Set_Game:

    # Tkinter setup
    # The tk window will be our "table" for the card card
    # table = tk.Tk()
    # table.title("Set Game")
    # table.geometry("800x500")
    # table.config(bg="grey")

    # Number of cards in deck
    MAX_CARDS = 81
    # Keep track of th cards left in the deck.  When deck = 0, game is over
    card_deck = [i for i in range(MAX_CARDS)]
    # Value for each card, [0,0,0,0] ==> [Red, 1, Empty, Triangle]
    CARD_VALUES = [[0, 0, 0, 0] for i in range(MAX_CARDS)]
    # Each card is represented by a Tkinter button
    CARD_BUTTONS = [0 for i in range(MAX_CARDS)]
    card_pos = [[0, 0] for i in range(MAX_CARDS)]
    # Keep track of cards drawn
    # not sure if needed
    # cards_drawn = [False for i in range(MAX_CARDS)]

    # Keep track of which cards are selected on table
    card_selected = [False for i in range(MAX_CARDS)]
    # Save the selected cards in a list to check if the set of 3 is a Set
    card_set = []

    # Keep track of available spots for cards on the table
    # Use this to add new cards when sets are made
    # 1 ==> Spot taken, 0 ==> Spot free
    card_table = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

    def __init__(self, master):

        # Use the frame initialize in main.py
        self.master = master

        # Get the images
        self.CARD_IMAGE_PATHS = glob.glob("Setcards\*.png")
        # The order of the cards matters
        # The ternary value representing the card is based on its place in line
        self.CARD_IMAGE_PATHS = sorted(
            self.CARD_IMAGE_PATHS, key=lambda n: int(re.findall(r"\d+", n)[0])
        )
        self.card_images = []
        for i in range(self.MAX_CARDS):
            self.card_image = tk.PhotoImage(file=self.CARD_IMAGE_PATHS[i])
            self.card_images.append(self.card_image)

        # In case you want to display the ternary value on the card buttons
        self.button_font = tkfont.Font(family="System", size=8, weight="bold")

        for i in range(self.MAX_CARDS):

            # Create a ternary value to represent each card
            self.CARD_VALUES[i] = self.ternary(i)

            button_text = str(i) + ": " + str(self.CARD_VALUES[i])
            # Create a button for each card
            card = tk.Button(
                self.master,
                image=self.card_images[i],
                font=self.button_font,
                text=button_text,
                bg="black",
                fg="white",
                compound="top",
                # height=5,
                # width=10,
                command=partial(self.card_click, i),
            )
            # Add it to the list
            self.CARD_BUTTONS[i] = card

    # Each card can be represented by a 4 digit ternary value
    # For example, a Red, Empty, Single, Circle is [0,0,0,0]
    def ternary(self, n):
        if n == 0:
            return [0, 0, 0, 0]
        num = []
        while n:
            n, r = divmod(n, 3)
            num.append(r)
        num = num[::-1]
        if len(num) == 1:
            num.insert(0, 0)
            num.insert(0, 0)
            num.insert(0, 0)
            return num
        elif len(num) == 2:
            num.insert(0, 0)
            num.insert(0, 0)
            return num
        elif len(num) == 3:
            num.insert(0, 0)
            return num
        elif len(num) == 4:
            return num

    def new_game(self):

        # Create a deck
        self.card_deck = [i for i in range(self.MAX_CARDS)]
        # Shuffle the deck
        random.shuffle(self.card_deck)

        # Lay 12 cards out on the table to form a grid
        # Orientation now very important, 3 rows by 4 columns fits better though
        for i in range(3):
            for j in range(4):

                # Pick cards from the deck
                self.card_picked = self.card_deck[0]
                print(self.card_picked, " ", end="")
                # Place them into the frame
                self.CARD_BUTTONS[self.card_picked].grid(
                    row=i, column=j, padx=10, pady=10
                )
                # Keep track of positions
                self.card_pos[self.card_picked] = i, j
                # Keep track of available spots on table
                self.card_table[i][j] = 1

                # Remove the picked cards from the deck
                self.card_deck.pop(0)
            print()
        print("Cards Left: {}".format(self.cards_left()))

    # Add three more cards to the table
    def draw_three(self):
        for i in range(3):
            new_card = self.card_deck[0]
            self.CARD_BUTTONS[new_card].grid(row=i, column=5)
            self.card_deck.pop(0)
            # print("Cards Left: {}".format(self.cards_left()))

    def cards_left(self):
        return str(len(self.card_deck))

    def card_click(self, num):

        self.card_selected[num] = not self.card_selected[num]
        # print(self.CARD_VALUES[num])
        # print(self.card_pos[num])

        if self.card_selected[num] == True:

            if len(self.card_set) < 3:
                self.card_set.append(num)
                self.CARD_BUTTONS[num].config(bg="green")
                print(self.card_set)

        elif self.card_selected[num] == False:
            if num in self.card_set:
                self.index = self.card_set.index(num)
                self.card_set.pop(self.index)
                self.CARD_BUTTONS[num].config(bg="black")
            print(self.card_set)

    def check_set(self):

        if len(self.card_set) == 3:

            card_1 = self.CARD_VALUES[self.card_set[0]]
            card_2 = self.CARD_VALUES[self.card_set[1]]
            card_3 = self.CARD_VALUES[self.card_set[2]]

            if (
                (
                    card_1[0] == card_2[0] == card_3[0]
                    or card_1[0] != card_2[0] != card_3[0]
                )
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
                # Take these cards off the table
                self.CARD_BUTTONS[self.card_set[0]].grid_forget()
                self.CARD_BUTTONS[self.card_set[1]].grid_forget()
                self.CARD_BUTTONS[self.card_set[2]].grid_forget()
                # Get the grid location of these cards
                card_1_x, card_1_y = self.card_pos[self.card_set[0]]
                card_2_x, card_2_y = self.card_pos[self.card_set[1]]
                card_3_x, card_3_y = self.card_pos[self.card_set[2]]

                # Place a card at the first location
                self.CARD_BUTTONS[self.card_deck[0]].grid(
                    row=card_1_x,
                    column=card_1_y,
                    padx=10,
                    pady=10,
                )
                # Remove this card from the deck
                self.card_deck.pop(0)

                # Repeat 2 more times
                self.CARD_BUTTONS[self.card_deck[0]].grid(
                    row=card_2_x,
                    column=card_2_y,
                    padx=10,
                    pady=10,
                )
                self.card_deck.pop(0)

                self.CARD_BUTTONS[self.card_deck[0]].grid(
                    row=card_3_x,
                    column=card_3_y,
                    padx=10,
                    pady=10,
                )
                self.card_deck.pop(0)

                # Clear out the card_set[]
                self.card_set.pop(0)
                self.card_set.pop(0)
                self.card_set.pop(0)

            else:
                print("Not A Set!")

        else:
            print("Need A Full Set!")
