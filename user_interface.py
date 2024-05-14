from tkinter import *
from tkinter import simpledialog
import easygui

BACKGROUND_COLOUR = "#9195F6"
BUTTON_COLOUR = "#F94892"
CROSS_COLOUR = "#10439F"
CIRCLE_COLOUR = "#F94A29"


def get_player_one():
    player_1 = easygui.enterbox("What's your name?\n You'll be player 1:", "Input")  # Set timeout to 5 seconds
    if player_1 is not None:
        pass
        # Process the user input here
    else:
        pass
        # Handle the case where the timeout occurs


def get_player_two():
    player_2 = easygui.enterbox("What's your name?\n You'll be player 2:", "Input")  # Set timeout to 5 seconds
    if player_2 is not None:
        pass
        # Process the user input here
    else:
        pass
        # Handle the case where the timeout occurs


get_player_one()
get_player_two()
app = Tk()
app.title("Tic-tac-toe")
# app.geometry("900x600")
app.config(padx=30, pady=20, bg=BACKGROUND_COLOUR)

# Load the image
front = PhotoImage(file="images/colourful_grid.png")

# Calculate the size of the image
image_width = front.width()
image_height = front.height()

# Calculate the scaling factor to fit the image within the available space
max_width = 430  # Maximum width of the canvas
max_height = 430  # Maximum height of the canvas
scale = min(max_width / image_width, max_height / image_height)

# Resize the image
image_width = int(image_width * scale)
image_height = int(image_height * scale)
front_resized = front.subsample(round(1 / scale), round(1 / scale))  # Resample the image to fit the canvas

# Create a canvas with the resized image
display_canvas = Canvas(app, width=max_width, height=max_height, bg=BACKGROUND_COLOUR, highlightthickness=0)
display_canvas.create_image(max_width / 2, max_height / 2, image=front_resized)
word_text = display_canvas.create_text(325, 235, text="✖️", fill=CROSS_COLOUR, font=("calibri", 120))
display_canvas.grid(row=1, column=1, columnspan=2, pady=20)

play_image = PhotoImage(file="images/black_play.png")

right_button = Button(bg=BUTTON_COLOUR, image=play_image, highlightthickness=0, )
wrong_button = Button(highlightthickness=0, )
right_button.grid(row=2, column=2)
wrong_button.grid(row=2, column=1)


def get_user_input():
    user_input = simpledialog.askstring("Input", "Enter your text:")
    if user_input is not None:
        pass
        # Process the user input here
    else:
        pass
        # Handle the case where the user cancels the dialog


# Create a button to trigger the input dialog
button = Button(text="Get Input", command=get_user_input)
button.grid(row=2, column=3)

# Trigger the input popup automatically


app.mainloop()
