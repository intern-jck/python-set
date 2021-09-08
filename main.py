import set_game
import tkinter as tk

table = tk.Tk()

game = set_game.Set_Game(table)

table.title("Set Game")
table.geometry("800x500")
table.config(bg="grey")

new_game_button = tk.Button(table, text="New Game", command=game.new_game)
draw_three_button = tk.Button(table, text="Draw 3", command=game.draw_three)
check_set_button = tk.Button(table, text="Check Set", command=game.check_set)

new_game_button.place(x=700, y=100)
draw_three_button.place(x=700, y=150)
check_set_button.place(x=700, y=200)

table.mainloop()
