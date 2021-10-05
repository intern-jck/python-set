import tkinter as tk
import tkinter.font as tkfont
from functools import partial
import random
import re
import glob

# Set Game


class Set_Game:

    # Number of cards in deck
    MAX_CARDS = 81

    # Value for each card, [0,0,0,0] ==> [Red, 1, Empty, Circle]
    CARD_VALUES = [[0, 0, 0, 0] for i in range(MAX_CARDS)]

    # Each card is represented by a Tkinter button
    CARD_BUTTONS = [0 for i in range(MAX_CARDS)]

    # Keep track of which cards are selected on table
    card_selected = [False for i in range(MAX_CARDS)]

    # Save the selected cards in a list to check if the set of 3 is a Set
    card_set = []

    # Keep track of available spots for cards on the table
    # Use this to add new cards when sets are made
    # 1 ==> Spot taken, 0 ==> Spot free
    CARD_TABLE_ROWS = 3
    CARD_TABLE_COLS = 5
    card_table = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

    def __init__(self, master):

        # Use the frame initialized in main.py
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
        self.button_font = tkfont.Font(family="System", size=10, weight="bold")

        # Create each card
        for i in range(self.MAX_CARDS):

            # Create a ternary value to represent each card
            self.CARD_VALUES[i] = self.ternary(i)
            # Text to show button card number and value
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
                command=partial(self.card_click, i),
            )
            # Add it to the list
            self.CARD_BUTTONS[i] = card

    # Function to create a ternary value based on input
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

    def easy_game(self):

        self.card_deck = [i for i in range(self.MAX_CARDS)]
        print(self.card_deck)

        for i in range(3):
            for j in range(4):

                # Pick cards from the deck
                new_card = self.draw_card()

                # Place them into the frame
                self.CARD_BUTTONS[new_card].grid(row=i, column=j, padx=10, pady=10)

                # Keep track of available spots on table
                self.card_table[i][j] = new_card

                print(" {}, ".format(self.card_table[i][j]), end=" ")

            print()
        print("Cards Left: {}".format(self.cards_left()))

    def new_game(self):

        # Create a deck
        self.card_deck = [i for i in range(self.MAX_CARDS)]
        # print(self.card_deck)

        # shuffle the deck
        random.shuffle(self.card_deck)
        # print(self.card_deck)

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

                print(" {}, ".format(self.card_table[i][j]), end=" ")
            print()

    # Add three more cards to the table
    def draw_three(self):
        for i in range(3):

            new_card = self.card_deck[self.draw_card()]

            self.CARD_BUTTONS[new_card].grid(row=i, column=5)
            self.card_table[i][4] = new_card

    def cards_left(self):
        return str(len(self.card_deck))

    def card_click(self, num):

        self.card_selected[num] = not self.card_selected[num]
        # print(self.CARD_VALUES[num])
        # print(self.card_pos[num])
        # print(self.CARD_BUTTONS[num].grid_info())

        if self.card_selected[num] == True:

            if len(self.card_set) < 3:
                self.card_set.append(num)
                self.CARD_BUTTONS[num].config(bg="green")
                print(self.card_set)
                card_info = self.CARD_BUTTONS[num].grid_info()
                print(card_info["row"], card_info["column"])

        elif self.card_selected[num] == False:

            if num in self.card_set:
                self.index = self.card_set.index(num)
                self.card_set.pop(self.index)
                self.CARD_BUTTONS[num].config(bg="black")
            print(self.card_set)

    def check_set(self):

        # If there are 3 cards selected
        if len(self.card_set) == 3:
            # Get the ternary values for each card
            card_1 = self.CARD_VALUES[self.card_set[0]]
            card_2 = self.CARD_VALUES[self.card_set[1]]
            card_3 = self.CARD_VALUES[self.card_set[2]]

            # Comapare the three values
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
                # Get the grid positions of the three cards
                card_1_info = self.CARD_BUTTONS[self.card_set[0]].grid_info()
                card_2_info = self.CARD_BUTTONS[self.card_set[1]].grid_info()
                card_3_info = self.CARD_BUTTONS[self.card_set[2]].grid_info()

                # Take these cards off the table
                self.CARD_BUTTONS[self.card_set[0]].grid_forget()
                self.CARD_BUTTONS[self.card_set[1]].grid_forget()
                self.CARD_BUTTONS[self.card_set[2]].grid_forget()

                # Place three new cards on the table
                new_card = self.draw_card()
                self.CARD_BUTTONS[new_card].grid(
                    row=card_1_info["row"],
                    column=card_1_info["column"],
                    padx=10,
                    pady=10,
                )

                # Repeat 2 more times
                new_card = self.draw_card()
                self.CARD_BUTTONS[new_card].grid(
                    row=card_2_info["row"],
                    column=card_2_info["column"],
                    padx=10,
                    pady=10,
                )

                new_card = self.draw_card()
                self.CARD_BUTTONS[new_card].grid(
                    row=card_3_info["row"],
                    column=card_3_info["column"],
                    padx=10,
                    pady=10,
                )

                # Clear out the Set if any left from previous game
                for i in range(len(self.card_set)):
                    self.card_set.pop(0)

            else:
                print("Not A Set!")

        else:
            print("Need A Full Set!")

    # def sort_table(self):
    #     current_table = []
    #     for i in self.CARD_TABLE_ROWS:
    #         for j in self.CARD_TABLE_COLS:
    #             if self.card_table[i][j] == 1:
    #                 cuurent_table.append(self)

    def draw_card(self):
        # Draw a card from the deck
        new_card = self.card_deck[0]
        # Remove this card from the deck
        self.card_deck.pop(0)
        return new_card
