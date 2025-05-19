import tkinter as tk
from tkinter import messagebox

def check_winner():
    for combo in [[0, 1, 2], [3, 4, 5], [6, 7, 8], 
                  [0, 3, 6], [1, 4, 7], [2, 5, 8], 
                  [0, 4, 8], [2, 4, 6]]:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            for i in combo:
                buttons[i].config(bg="green")
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[combo[0]]['text']} wins!")
            global winner
            winner = True
            return

def button_click(index):
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player
        check_winner()
        if not winner:
            toggle_player()

def toggle_player():
    global current_player
    current_player = "X" if current_player == "O" else "O"
    label.config(text=f"Player: {current_player}'s turn")

# Initialize window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Track current player and winner
current_player = "X"
winner = False

# Create label
label = tk.Label(root, text="Player: X's turn", font=("normal", 15))
label.grid(row=0, column=0, columnspan=3)

# Create buttons
buttons = []
for i in range(9):
    btn = tk.Button(root, text="", font=("normal", 25), width=6, height=2,
                    command=lambda i=i: button_click(i))
    btn.grid(row=(i // 3) + 1, column=i % 3)  # +1 because label is on row 0
    buttons.append(btn)

# Run the GUI loop
root.mainloop()
