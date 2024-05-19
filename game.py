from tkinter import *
from tkinter import simpledialog, messagebox
import easygui

# colour schemes
BACKGROUND_COLOUR = "#9195F6"
BUTTON_COLOUR = "#F94892"
CROSS_COLOUR = "#10439F"
CIRCLE_COLOUR = "#F94A29"
NUMERICAL_COLOUR = "#211C6A"

# character positioning
positions = {
    "01": (78, 80),
    "02": (215, 80),
    "03": (352, 80),
    "04": (78, 215),
    "05": (215, 215),
    "06": (352, 215),
    "07": (78, 354),
    "08": (215, 354),
    "09": (352, 354),
}


def get_player_one():
    player_1 = easygui.enterbox("What's your name?\n You'll be player 1✖️:", "Input")
    return player_1
    if player_1 is not None:
        pass
    else:
        pass


def get_player_two():
    player_2 = easygui.enterbox("What's your name?\n You'll be player 2:", "Input")
    if player_2 is not None:
        pass
        # Process the user input here
    else:
        pass
        # Handle the case where the timeout occurs


def choose_position(player):
    """goes to the position the player chooses"""
    # if player == self.player_1:
    #     character = "❌"
    # else:
    #     character = "⭕"
    # # print(self.board)
    response = input(f"where do you want to make your move {player}🤔: ")
    if len(response) == 1:
        while True:
            messagebox.showwarning(
                "Error", "Please include 0 in your answer. eg '01' and not 1"
            )
            response = input(f"where do you want to make your move {player}🤔\n")
            if len(response) != 1:
                break


player = get_player_one()
get_player_two()
# choose_position(player)
app = Tk()
app.title("Tic-tac-toe")
# app.geometry("900x600")
app.config(padx=30, pady=20, bg=BACKGROUND_COLOUR)

# board image
board = PhotoImage(file="images/colourful_grid.png")
image_width = board.width()
image_height = board.height()

# canvas setup
max_width = 430
max_height = 430
scale = min(max_width / image_width, max_height / image_height)
image_width = int(image_width * scale)
image_height = int(image_height * scale)
board_resized = board.subsample(round(1 / scale), round(1 / scale))

# default canvas
display_canvas = Canvas(
    app, width=max_width, height=max_height, bg=BACKGROUND_COLOUR, highlightthickness=0
)
display_canvas.create_image(max_width / 2, max_height / 2, image=board_resized)
num_1 = display_canvas.create_text(
    positions["01"], text="01", fill=NUMERICAL_COLOUR, font=("calibri", 90)
)
num_2 = display_canvas.create_text(
    positions["02"], text="02", fill=NUMERICAL_COLOUR, font=("calibri", 90)
)
num_3 = display_canvas.create_text(
    positions["03"], text="03", fill=NUMERICAL_COLOUR, font=("calibri", 90)
)
num_4 = display_canvas.create_text(
    positions["04"], text="04", fill=NUMERICAL_COLOUR, font=("calibri", 90)
)
num_5 = display_canvas.create_text(
    positions["05"], text="05", fill=NUMERICAL_COLOUR, font=("calibri", 90)
)
num_6 = display_canvas.create_text(
    positions["06"], text="06", fill=NUMERICAL_COLOUR, font=("calibri", 90)
)
num_7 = display_canvas.create_text(
    positions["07"], text="07", fill=NUMERICAL_COLOUR, font=("calibri", 90)
)
num_8 = display_canvas.create_text(
    positions["08"], text="08", fill=NUMERICAL_COLOUR, font=("calibri", 90)
)
num_9 = display_canvas.create_text(
    positions["09"], text="09", fill=NUMERICAL_COLOUR, font=("calibri", 90)
)
display_canvas.grid(row=1, column=1, columnspan=2, pady=20)

# play button
play_image = PhotoImage(file="images/black_play.png")
play_button = Button(bg=BUTTON_COLOUR, image=play_image, highlightthickness=0)
play_button.grid(row=2, column=1)


def get_user_input():
    user_input = simpledialog.askstring("Input", "Where do you wanna go:")
    response = input(f"where do you want to make your move {player}🤔: ")
    if len(response) == 1:
        while True:
            messagebox.showwarning(
                "Error", "Please include 0 in your answer. eg '01' and not 1"
            )
            response = input(f"where do you want to make your move {player}🤔\n")
            if len(response) != 1:
                break
    if user_input is not None:
        pass
        # Process the user input here
    else:
        pass
        # Handle the case where the user cancels the dialog


# Create a button to trigger the input dialog
button = Button(text="Get Input", command=get_user_input)
button.grid(row=2, column=2)

app.mainloop()
