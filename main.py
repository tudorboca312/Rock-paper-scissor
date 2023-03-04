import tkinter as tk
from PIL import Image,ImageTk
import random
import winsound

# Functions

# Sounds
def winSound():
    sound_file_win = 'win.wav'
    winsound.PlaySound(sound_file_win, winsound.SND_ASYNC)
def loseSound():
    sound_file_lose = 'lose.wav'
    winsound.PlaySound(sound_file_lose, winsound.SND_ASYNC)
def tieSOund():
    sound_file_tie = 'tie.wav'
    winsound.PlaySound(sound_file_tie, winsound.SND_ASYNC)


# Computer random choice
def computer_choice(x):
    global computer_label  # add this line
    random_number = x
    if computer_label:
        computer_label.destroy()
    computer_label = tk.Label(root, image=images_cp[random_number], bg="#BF40BF")
    computer_label.place(relx=0.85, rely = 0.5, anchor="center")

# User choice + calling the computer's
def choose(choice, x):
    global user_label
    if choice == "rock":
        # Check if there is a previous user_label and destroy it
        if user_label:
            user_label.destroy()
        user_label = tk.Label(root, image=rock_new, bg="#BF40BF")
        user_label.place(relx=0.15, rely = 0.5, anchor="center")
        computer_choice(x)
    elif choice == "scissor":
        if user_label:
            user_label.destroy()
        user_label = tk.Label(root, image=scissor_new, bg="#BF40BF")
        user_label.place(relx=0.15, rely = 0.5, anchor="center")
        computer_choice(x)
    elif choice == "papper":
        if user_label:
            user_label.destroy()
        user_label = tk.Label(root, image=papper_new, bg="#BF40BF")
        user_label.place(relx=0.15, rely = 0.5, anchor="center")
        computer_choice(x)
    else:
        print("Not yet!")


# Pressing the button and calling all the functions
def pressed(choice, x):
    global winner
    global score_points
    global scoreNumber
    choose(choice, x)
    if choice == "rock" and x == 0:
        if winner:
            winner.destroy()
        winner = tk.Label(root, text="Tie!", font=("Arial", 24), bg="#BF40BF", fg="#fff")
        winner.place(relx=0.5, rely=0.5, anchor='center')
        tieSOund()
    elif choice == "rock" and x == 1:
        if winner:
            winner.destroy()
        winner = tk.Label(root, text="You win!", font=("Arial", 24), bg="#BF40BF", fg="#fff")
        winner.place(relx=0.5, rely=0.5, anchor='center')
        winSound()
        score_points = score_points+1   
        scoreNumber = tk.Label(root, text=score_points, font=("Arial", 20), bg="#BF40BF", fg="#fff")
        scoreNumber.place(relx=0.535, rely=0.2, anchor='center')
    elif choice == "rock" and x == 2:
        if winner:
            winner.destroy()
        winner = tk.Label(root, text="You lose!", font=("Arial", 24), bg="#BF40BF", fg="#fff")
        winner.place(relx=0.5, rely=0.5, anchor='center')
        loseSound()
        if score_points > 0:
          score_points = score_points-1
        scoreNumber = tk.Label(root, text=score_points, font=("Arial", 20), bg="#BF40BF", fg="#fff")
        scoreNumber.place(relx=0.535, rely=0.2, anchor='center')
    elif choice == "papper" and x == 0:
        if winner:
            winner.destroy()
        winner = tk.Label(root, text="You win!", font=("Arial", 24), bg="#BF40BF", fg="#fff")
        winner.place(relx=0.5, rely=0.5, anchor='center')  
        winSound() 
        score_points = score_points+1
        scoreNumber = tk.Label(root, text=score_points, font=("Arial", 20), bg="#BF40BF", fg="#fff")
        scoreNumber.place(relx=0.535, rely=0.2, anchor='center')
    elif choice == "papper" and x == 1:
        if winner:
            winner.destroy()
        winner = tk.Label(root, text="You lose!", font=("Arial", 24), bg="#BF40BF", fg="#fff")
        winner.place(relx=0.5, rely=0.5, anchor='center')
        loseSound()
        if score_points > 0:
          score_points = score_points-1
        scoreNumber = tk.Label(root, text=score_points, font=("Arial", 20), bg="#BF40BF", fg="#fff")
        scoreNumber.place(relx=0.535, rely=0.2, anchor='center')
    elif choice == "papper" and x == 2:
        if winner:
            winner.destroy()
        winner = tk.Label(root, text="Tie!", font=("Arial", 24), bg="#BF40BF", fg="#fff")
        winner.place(relx=0.5, rely=0.5, anchor='center')
        tieSOund()
    elif choice == "scissor" and x == 0:
        if winner:
            winner.destroy()
        winner = tk.Label(root, text="You lose!", font=("Arial", 24), bg="#BF40BF", fg="#fff")
        winner.place(relx=0.5, rely=0.5, anchor='center') 
        loseSound()
        if score_points > 0:
          score_points = score_points-1
        scoreNumber = tk.Label(root, text=score_points, font=("Arial", 20), bg="#BF40BF", fg="#fff")
        scoreNumber.place(relx=0.535, rely=0.2, anchor='center')
    elif choice == "scissor" and x == 1:
        if winner:
            winner.destroy()
        winner = tk.Label(root, text="Tie!", font=("Arial", 24), bg="#BF40BF", fg="#fff")
        winner.place(relx=0.5, rely=0.5, anchor='center')
        tieSOund()
    elif choice == "scissor" and x == 2:
        if winner:
            winner.destroy()
        winner = tk.Label(root, text="You win!", font=("Arial", 24), bg="#BF40BF", fg="#fff")
        winner.place(relx=0.5, rely=0.5, anchor='center')
        winSound()
        score_points = score_points+1
        scoreNumber = tk.Label(root, text=score_points, font=("Arial", 20), bg="#BF40BF", fg="#fff")
        scoreNumber.place(relx=0.535, rely=0.2, anchor='center')
        
# Reset the game
def reset():
    global winner
    global score_points
    global scoreNumber
    global computer_label
    global user_label
    score_points = 0
    scoreNumber = tk.Label(root, text=score_points, font=("Arial", 20), bg="#BF40BF", fg="#fff")
    scoreNumber.place(relx=0.535, rely=0.2, anchor='center')

    if winner:
            winner.destroy()

    if computer_label:
        computer_label.destroy()
    if user_label:
        user_label.destroy()

    user_label = tk.Label(root, image=rock_new, bg="#BF40BF")
    user_label.place(relx=0.15, rely = 0.5, anchor="center")

    computer_label = tk.Label(root, image=rock_cp_new, bg="#BF40BF")
    computer_label.place(relx=0.85, rely = 0.5, anchor="center")


# Creating the window with all the features

# Main window
root = tk.Tk()

# Creating the window size
root.geometry("1000x600")

# Make sure can't resize the window
root.resizable(False, False)
# Window background color
root.configure(bg="#BF40BF")

# Main Header and its styiling
mainHeader = tk.Label(root, text="Welcome to Rock, Papper, Scissor", font=("Arial", 26, "bold"), bg="#BF40BF", fg="#fff")
mainHeader.place(relx=0.5, rely=0.1, anchor='center')

# Score
score_points = 0
score = tk.Label(root, text="Score: ", font=("Arial", 20), bg="#BF40BF", fg="#fff")
score.place(relx=0.48, rely=0.2, anchor='center')
scoreNumber = tk.Label(root, text=score_points, font=("Arial", 20), bg="#BF40BF", fg="#fff")
scoreNumber.place(relx=0.535, rely=0.2, anchor='center')

# Open Image
scissor_pic = Image.open("scissor.png")
rock_pic = Image.open("rock.png")
papper_pic = Image.open("papper.png")
scissor_cp = Image.open("scissor_cp.png")
papper_cp = Image.open("papper_cp.png")
rock_cp = Image.open("rock_cp.png")


# Resize Image
resized_scissor = scissor_pic.resize((200, 200), Image.LANCZOS)
resized_rock = rock_pic.resize((180, 180), Image.LANCZOS)
resized_papper = papper_pic.resize((220, 220), Image.LANCZOS)
resized_rock_cp = rock_cp.resize((200, 200), Image.LANCZOS)
resized_scissor_cp = scissor_cp.resize((180, 180), Image.LANCZOS)
resized_papper_cp = papper_cp.resize((220, 220), Image.LANCZOS)

scissor_new = ImageTk.PhotoImage(resized_scissor)
rock_new = ImageTk.PhotoImage(resized_rock)
papper_new = ImageTk.PhotoImage(resized_papper)
rock_cp_new = ImageTk.PhotoImage(resized_rock_cp)
scissor_cp_new = ImageTk.PhotoImage(resized_scissor_cp)
papper_cp_new = ImageTk.PhotoImage(resized_papper_cp)

images_cp = [
    rock_cp_new, scissor_cp_new, papper_cp_new
]


# Insert images to the tkinter
user_label = tk.Label(root, image=scissor_new, bg="#BF40BF")
user_label.place(relx=0.15, rely = 0.5, anchor="center")

computer_label = tk.Label(root, image=rock_cp_new, bg="#BF40BF")
computer_label.place(relx=0.85, rely = 0.5, anchor="center")

# Insert winner
winner = tk.Label(root, text="You win!", font=("Arial", 24), bg="#BF40BF", fg="#fff")
winner.place(relx=0.5, rely=0.5, anchor='center')

# Buttons
# Create buttons with different colors
rock_button = tk.Button(root, text="Rock", bg="#B2D8B2", fg="#000", width=12, height=1, command=lambda:pressed("rock", random.randint(0, 2)))
papper_button = tk.Button(root, text="Papper", bg="#D8B2D8", fg="#000", width=12, command=lambda:pressed("papper", random.randint(0, 2)))
scissor_button = tk.Button(root, text="Scissor", bg="#FFB347", fg="#000", width=12, command=lambda:pressed("scissor", random.randint(0, 2)))
reset_button = tk.Button(root, text="Reset", bg="#E8A2E6", fg="#000", width=12, command=lambda:reset())


# Place buttons at relx: 0.8, rely: 0.8
rock_button.place(relx=0.4, rely=0.9, anchor='center')
papper_button.place(relx=0.5, rely=0.9, anchor='center')
scissor_button.place(relx=0.6, rely=0.9, anchor='center')
reset_button.place(relx=0.5, rely=0.95, anchor='center')

root.mainloop()

