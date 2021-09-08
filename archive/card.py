import tkinter as tk
from functools import partial
import random

# Set Game


class Set_Game:

    # Tkinter setup
    # The tk window will be our "table" for the card card
    table = tk.Tk()
    table.title("Set Game")
    table.geometry("800x500")
    table.config(bg="grey")

    # Number of cards in deck
    MAX_CARDS = 81
    # Keep track of th cards left in the deck.  When deck = 0, game is over
    card_deck = [i for i in range(MAX_CARDS)]
    # Value for each card, [0,0,0,0] ==> [Red, 1, Empty, Triangle]
    CARD_VALUES = [[0, 0, 0, 0] for i in range(MAX_CARDS)]
    # Each card is represented by a Tkinter button
    CARD_BUTTONS = [0 for i in range(MAX_CARDS)]

    # Keep track of cards drawn
    # not sure if needed
    # cards_drawn = [False for i in range(MAX_CARDS)]

    # Keep track of which cards are selected on table
    card_selected = [False for i in range(MAX_CARDS)]
    # Save the selected cards in a list to check if the set of 3 is a Set
    card_set = []

    def __init__(self):

        # # Clear out the set if any cards are present
        # for i in range(len(self.card_set)):
        #     self.card_set.pop(i)

        for i in range(self.MAX_CARDS):
            # Create a button for each card
            card = tk.Button(
                self.table,
                bg="black",
                height=5,
                width=10,
                command=partial(self.card_click, i),
            )
            # Add it to the list
            self.CARD_BUTTONS[i] = card

        # Shuffle the deck
        random.shuffle(self.card_deck)

        # Lay 12 cards out on the table to form a grid
        # Orientation now very important, 3 rows by 4 columns fits better though
        for i in range(3):
            for j in range(4):

                self.card_picked = self.card_deck[0]
                print(self.card_picked, " ", end="")
                self.CARD_BUTTONS[self.card_picked].place(
                    x=40 + j * 100, y=40 + i * 140
                )
                self.card_deck.pop(0)

            print()

        self.table.mainloop()

    def card_click(self, num):
        self.card_selected[num] = not self.card_selected[num]

        if self.card_selected[num] == True:

            if len(self.card_set) < 3:
                self.card_set.append(num)
                self.CARD_BUTTONS[num].config(bg="red")
                print(self.card_set)

        elif self.card_selected[num] == False:
            if num in self.card_set:
                self.index = self.card_set.index(num)
                self.card_set.pop(self.index)
                self.CARD_BUTTONS[num].config(bg="black")
            print(self.card_set)

    def draw_three(self):
        for i in range(3):
            self.card_buttons[i].place(x=440, y=40 + i * 140)


    


set = Set_Game()
