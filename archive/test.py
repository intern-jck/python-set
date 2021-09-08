import tkinter as tk


def clicked(event):
    print(f"You clicked at {event.x} X {event.y}.")


root = tk.Tk()
drawCanv = tk.Canvas(width=541, height=301, bd=0)
drawCanv.bind("<Button>", clicked)

for x in range(1, 540, 60):
    for y in range(1, 300, 60):
        rectangle = drawCanv.create_rectangle(x, y, x + 60, y + 60, outline="black")
drawCanv.pack()

tk.mainloop()
