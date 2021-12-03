import tkinter as tk
import tkinter.font as tkfont
from functools import partial
import random
import re
import glob


class Set_Game:

    # Number of cards in deck
    DECK_SIZE = 81
    # A deck is simply range of numbers up to deck size
    DECK = [i for i in range(DECK_SIZE)]

    # CARDS.  May make its own class
    # Each card is represented by a Tkinter button
    CARD_BUTTONS = [0 for i in range(DECK_SIZE)]
    CARD_IMAGES = [0 for i in range(DECK_SIZE)]

    # Value for each card [Color, Texture, Amount, Shape]
    # [0,0,0,0] ==> [Red, Empty, 1, Triangle]
    # Create empty set of values
    CARD_VALUES = [0 for i in range(DECK_SIZE)]

    # Keep track of which cards are selected on table
    card_selected = [False for i in range(DECK_SIZE)]

    # Save each card selected to check if they make a Set
    card_set = []
    set = []
    # alt_card_deck = [[0, 0] for i in range(DECK_SIZE)]

    # Card Table is a grid 3 x 5
    TABLE_ROW = 3
    TABLE_COL = 5

    def __init__(self, master):

        # Use the frame initialized in main.py
        self.master = master

        # Get the images
        self.CARD_IMAGE_PATHS = glob.glob("cardArt\*.png")

        # The png files are named with the correct card number
        # Sort the files in order to put them in the proper order
        self.CARD_IMAGE_PATHS = sorted(
            self.CARD_IMAGE_PATHS, key=lambda n: int(re.findall(r"\d+", n)[0])
        )

        for i in range(self.DECK_SIZE):
            self.card_image = tk.PhotoImage(file=self.CARD_IMAGE_PATHS[i])
            self.CARD_IMAGES[i] = self.card_image

        self.card_table = [
            [None, None, None, None, None],
            [None, None, None, None, None],
            [None, None, None, None, None],
        ]

        # Use to display button text
        self.button_font = tkfont.Font(family="System", size=10, weight="bold")

        # Create each card
        for i in range(self.DECK_SIZE):

            # Create a ternary value to represent each card
            self.CARD_VALUES[i] = self.ternary(i)

            # Text to show button card number and value
            button_text = str(i) + ": " + str(self.CARD_VALUES[i])

            # Create a button for each card
            card_button = tk.Button(
                self.master,
                image=self.CARD_IMAGES[i],
                font=self.button_font,
                text=button_text,
                bg="black",
                fg="white",
                compound="top",
                command=partial(self.card_click, i),
            )
            # Add it to the list
            self.CARD_BUTTONS[i] = card_button

            # List to store all cards and values
            # self.alt_card_deck[i] = [self.ternary(i), card_button]

    # Function to create a ternary value based on input
    def ternary(self, n):
        # Trivial case
        if n == 0:
            return [0, 0, 0, 0]

        # Create an array to store remainders
        num = []
        while n:
            n, r = divmod(n, 3)
            num.append(r)

        # Need to reverse array to properly format
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
        # self.card_deck = [i for i in range(self.DECK_SIZE)]
        # shuffle the deck
        # random.shuffle(self.card_deck)

        # Clear out the Set if any left from previous game
        for i in range(len(self.card_set)):
            self.card_set.pop(0)

        # Lay 12 cards out on the table to form a grid with 3 rows, 4 columns
        for i in range(3):
            for j in range(4):

                # Pick a card
                new_card = self.draw_card()

                # Place them into the frame
                self.CARD_BUTTONS[new_card].grid(row=i, column=j, padx=10, pady=10)

                # Keep track of cards on table
                self.card_table[i][j] = new_card

            #   print(" {}, ".format(self.card_table[i][j]), end=" ")
            # print()

    # def cards_left(self):
    #     return str(len(self.card_deck))

    def draw_card(self):
        # Draw a card from the deck
        new_card = self.DECK[0]
        # Remove this card from the deck
        self.DECK.pop(0)
        return new_card

    # # If no Set can be found, add three more cards to the end of the table
    def draw_three(self):
        for i in range(3):
            new_card = self.card_deck[self.draw_card()]
            self.CARD_BUTTONS[new_card].grid(row=i, column=5)
            self.card_table[i][4] = new_card

    # Clears the table

    def clear_table(self):

        for i in range(self.TABLE_ROW):
            for j in range(self.TABLE_COL):
                card_num = self.card_table[i][j]
                self.clear_card(card_num)

    def clear_card(self, card_num):

        card_info = self.CARD_BUTTONS[card_num].grid_info()
        row = card_info["row"]
        column = card_info["column"]
        # print(card_info, self.card_table[row][column])

        if self.card_table[row][column] is not None:
            self.card_table[row][column] = None
            self.CARD_BUTTONS[card_num].grid_forget()

    # Clears a selected set of cards
    def clear_set(self):

        for i in range(self.TABLE_ROW):
            for j in range(self.TABLE_COL):

                card_num = self.card_table[i][j]

                if card_num is not None and self.card_selected[card_num] == True:
                    self.clear_card(card_num)

        # Clear the set
        for i in range(len(self.set)):
            self.set.pop()

    def card_click(self, num):

        # Simple flag for selecting card
        self.card_selected[num] = not self.card_selected[num]
        # If selected...
        # Only allow up to three cards to be selected at once

        if self.card_selected[num] == True:
            if len(self.card_set) < 3:
                self.card_set.append(num)
                self.CARD_BUTTONS[num].config(bg="green")
                # print(self.card_set)
                # card_info = self.CARD_BUTTONS[num].grid_info()
                # print(card_info["row"], card_info["column"])

        elif self.card_selected[num] == False:
            if num in self.card_set:
                self.index = self.card_set.index(num)
                self.card_set.pop(self.index)
                self.CARD_BUTTONS[num].config(bg="black")
                # print(self.card_set)

    def check_set(self):

        # If there are 3 cards selected
        if len(self.card_set) == 3:

            # Get the cards in the set
            card_1 = self.card_set[0]
            card_2 = self.card_set[1]
            card_3 = self.card_set[2]

            # Get the values for each card
            card_1_val = self.CARD_VALUES[self.card_set[0]]
            card_2_val = self.CARD_VALUES[self.card_set[1]]
            card_3_val = self.CARD_VALUES[self.card_set[2]]

            # Comapare the three values
            if (
                (
                    card_1_val[0] == card_2_val[0] == card_3_val[0]
                    or card_1_val[0] != card_2_val[0] != card_3_val[0]
                )
                and (
                    card_1_val[1] == card_2_val[1] == card_3_val[1]
                    or card_1_val[1] != card_2_val[1] != card_3_val[1]
                )
                and (
                    card_1_val[2] == card_2_val[2] == card_3_val[2]
                    or card_1_val[2] != card_2_val[2] != card_3_val[2]
                )
                and (
                    card_1_val[3] == card_2_val[3] == card_3_val[3]
                    or card_1_val[3] != card_2_val[3] != card_3_val[3]
                )
            ):
                print("Set Found!")
                # Get the grid positions of the three cards
                card_1_info = self.CARD_BUTTONS[card_1].grid_info()
                card_2_info = self.CARD_BUTTONS[card_2].grid_info()
                card_3_info = self.CARD_BUTTONS[card_3].grid_info()

                # Take these cards off the table
                self.clear_card(card_1)
                self.clear_card(card_2)
                self.clear_card(card_3)
                # self.CARD_BUTTONS[card_1].grid_forget()
                # self.CARD_BUTTONS[card_2].grid_forget()
                # self.CARD_BUTTONS[card_3].grid_forget()

                # Place three new cards on the table
                new_card = self.draw_card()

                self.CARD_BUTTONS[new_card].grid(
                    row=card_1_info["row"],
                    column=card_1_info["column"],
                )

                # Repeat 2 more times
                new_card = self.draw_card()
                self.CARD_BUTTONS[new_card].grid(
                    row=card_2_info["row"],
                    column=card_2_info["column"],
                )

                new_card = self.draw_card()
                self.CARD_BUTTONS[new_card].grid(
                    row=card_3_info["row"],
                    column=card_3_info["column"],
                )

                # Clear out the Set
                for i in range(len(self.card_set)):
                    self.card_set.pop(0)

            else:
                print("Not A Set!")

        else:
            print("Need A Full Set!")
