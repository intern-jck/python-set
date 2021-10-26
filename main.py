import set_game
import tkinter as tk
import tkinter.font as tkfont

table = tk.Tk()

game = set_game.Set_Game(table)

table.title("Set Game")
table.geometry("800x500")
table.config(bg="grey")

button_font = tkfont.Font(family="Courier", size=10, weight="bold")

new_game_button = tk.Button(
    table, text="New Game", font=button_font, command=game.new_game
)
draw_three_button = tk.Button(
    table, text="Draw 3", font=button_font, command=game.draw_three
)
check_set_button = tk.Button(
    table, text="Check Set", font=button_font, command=game.check_set
)
# check_button = tk.Button(
#     table, text="Check Set", font=button_font, command=game.button_check
# )

easy_game_button = tk.Button(
    table, text="Easy Game", font=button_font, command=game.easy_game
)
cards_left = tk.StringVar()
cards_left.set(game.cards_left())

cards_left_label = tk.Label(table, textvariable=cards_left, relief="raised")
cards_left_label.place(x=600, y=50)

new_game_button.place(x=700, y=100)
draw_three_button.place(x=700, y=150)
check_set_button.place(x=700, y=200)
easy_game_button.place(x=700, y=400)


# Scoreboard
cards_left_label = tk.Label(table, text="Cards Left", font=button_font, relief="raised")
cards_left_label.place(x=600, y=50)


def update_score():
    cards_left_label.config(text="Cards Left:" + game.cards_left())
    table.after(250, update_score)


table.after(250, update_score)

table.mainloop()
