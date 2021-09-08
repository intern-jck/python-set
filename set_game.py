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

    # Keep track of cards drawn
    # not sure if needed
    # cards_drawn = [False for i in range(MAX_CARDS)]

    # Keep track of which cards are selected on table
    card_selected = [False for i in range(MAX_CARDS)]
    # Save the selected cards in a list to check if the set of 3 is a Set
    card_set = []

    def __init__(self, master):

        self.CARD_IMAGE_PATHS = glob.glob("Setcards\*.png")
        self.CARD_IMAGE_PATHS = sorted(
            self.CARD_IMAGE_PATHS, key=lambda n: int(re.findall(r"\d+", n)[0])
        )

        self.card_images = []
        for i in range(self.MAX_CARDS):
            self.card_image = tk.PhotoImage(file=self.CARD_IMAGE_PATHS[i])
            self.card_images.append(self.card_image)

        # # Clear out the set if any cards are present
        # for i in range(len(self.card_set)):
        #     self.card_set.pop(i)

        self.master = master
        self.button_font = tkfont.Font(family="Courier", size=10, weight="bold")

        for i in range(self.MAX_CARDS):

            # Create a ternary value to represent each card
            self.CARD_VALUES[i] = self.ternary(i)
            # Get an image for each card
            # print(self.card_images[i])
            # Create a button for each card
            card = tk.Button(
                self.master,
                image=self.card_images[i],
                # font=self.button_font,
                # text=str(self.CARD_VALUES[i]),
                bg="black",
                # height=5,
                # width=10,
                command=partial(self.card_click, i),
            )
            # Add it to the list
            self.CARD_BUTTONS[i] = card

    def new_game(self):

        # Shuffle the deck
        random.shuffle(self.card_deck)

        # Lay 12 cards out on the table to form a grid
        # Orientation now very important, 3 rows by 4 columns fits better though
        for i in range(3):
            for j in range(4):
                # pick cards from the deck
                self.card_picked = self.card_deck[0]
                print(self.card_picked, " ", end="")
                self.CARD_BUTTONS[self.card_picked].place(
                    x=40 + j * 100, y=40 + i * 140
                )
                # Remove the picked cards from the deck
                self.card_deck.pop(0)
            print()
        print("Cards Left: {}".format(self.cards_left()))

    def cards_left(self):
        return len(self.card_deck)

    def card_click(self, num):
        self.card_selected[num] = not self.card_selected[num]
        print(self.CARD_VALUES[num])

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
            new_card = self.card_deck[0]
            self.CARD_BUTTONS[new_card].place(x=440, y=40 + i * 140)
            self.card_deck.pop(0)
            print("Cards Left: {}".format(self.cards_left()))

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
                self.CARD_BUTTONS[self.card_set[0]].place_forget()
                self.CARD_BUTTONS[self.card_set[1]].place_forget()
                self.CARD_BUTTONS[self.card_set[2]].place_forget()
                # Find where they are in the deck
                self.index1 = self.card_deck.index(card_1)
                self.index2 = self.card_deck.index(card_2)
                self.index3 = self.card_deck.index(card_3)
                # Remove them from the deck
                self.card_deck.pop(self.index1)
                self.card_deck.pop(self.index2)
                self.card_deck.pop(self.index3)
                # Get the locations of the removed cards
                card_1_x, card_1_y = (
                    self.card_buttons[self.card_set[0]].winfo_rootx(),
                    self.card_buttons[self.card_set[0]].winfo_rooty(),
                )
                card_2_x, card_2_y = (
                    self.card_buttons[self.card_set[1]].winfo_rootx(),
                    self.card_buttons[self.card_set[1]].winfo_rooty(),
                )
                card_3_x, card_3_y = (
                    self.card_buttons[self.card_set[2]].winfo_rootx(),
                    self.card_buttons[self.card_set[2]].winfo_rooty(),
                )
                self.CARD_BUTTONS[self.card_deck[0]].place(x=card_1_x, y=card_1_y)
                self.card_deck.pop(0)

            else:
                print("Not A Set!")

        else:
            print("Need A Full Set!")

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


# set = Set_Game()
