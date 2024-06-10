class Game:
    """Represents tic-tac-toe game"""

    def __init__(self):
        self.board = """
        01❕02❕03
        ➖➕➖➕➖
        04❕05❕06
        ➖➕➖➕➖
        07❕08❕09
        """
        self.player_1 = input("What's your name? You are player 1\n")
        self.player_2 = input("What's your name? You are player 2\n")
        self.game_list = None

    def choose_position(self, player):
        """goes to the position the player chooses"""
        if player == self.player_1:
            character = "❌"
        else:
            character = "⭕"
        print(self.board)
        response = input(f"where do you want to make your move {player}🤔: ")
        if len(response) == 1:
            while True:
                print("\nPlease include 0 in your answer. eg '01' and not 1")
                response = input(f"where do you want to make your move {player}🤔\n")
                if len(response) != 1:
                    break

        # I have to make sure where the player plans to go exists, to prevent the code from crashing
        if response not in self.board:
            while True:
                print(
                    "\nThat position has been taken or doesn't exist. choose another!"
                )
                response = input(f"where do you want to make your move {player}🤔 ")
                if response in self.board:
                    break
        updated = self.board.replace(response, character)
        self.board = updated
        print(self.board)

    def get_score_board(self):
        """Produces a formatted score board in the form of lists, so I can work with it"""
        lines = [line.strip() for line in self.board.splitlines()]
        # Replace the unwanted characters in each line and convert the line to a list
        processed_lines = [
            list(
                line.replace("❕", "")
                .replace("➖", "")
                .replace("➕", "")
                .replace("0", "")
            )
            for line in lines
        ]
        # Filter out any empty lists from the processed lines
        self.game_list = [elements for elements in processed_lines if elements]

    def check_for_win(self):
        """Checks and finds out if there's a winner"""
        self.get_score_board()

        # Checks for horizontal wins
        for item in self.game_list:
            if all(element == "⭕" for element in item) or all(
                element == "❌" for element in item
            ):
                return True

        # Checks for diagonal wins
        if (
            self.game_list[0][0] == "⭕"
            and self.game_list[1][1] == "⭕"
            and self.game_list[2][2] == "⭕"
        ) or (
            self.game_list[0][2] == "⭕"
            and self.game_list[1][1] == "⭕"
            and self.game_list[2][0] == "⭕"
        ):
            return True
        if (
            self.game_list[0][0] == "❌"
            and self.game_list[1][1] == "❌"
            and self.game_list[2][2] == "❌"
        ) or (
            self.game_list[0][2] == "❌"
            and self.game_list[1][1] == "❌"
            and self.game_list[2][0] == "❌"
        ):
            return True

        # Checks for vertical wins
        if all(element[0] == "⭕" for element in self.game_list) or all(
            element[0] == "❌" for element in self.game_list
        ):
            return True
        if all(element[1] == "⭕" for element in self.game_list) or all(
            element[1] == "❌" for element in self.game_list
        ):
            return True
        if all(element[2] == "⭕" for element in self.game_list) or all(
            element[2] == "❌" for element in self.game_list
        ):
            return True

        return False

    def get_winner(self):
        """gets the user who won the match/round"""
        if current_round % 2 == 0:
            winner = self.player_1
            print(f"{winner} wins the match🥳🍾")
        else:
            winner = self.player_2
            print(f"{winner} wins the match🥳🍾")


# create an object for the class
game = Game()

# logic of game
game_not_over = True
current_round = 0
while game_not_over:

    # if the game goes to the end without a winner, we have a draw
    if current_round > 8:
        print("A hard fought draw 🤝")
        break

    if current_round % 2 == 0:
        user = game.player_1
    else:
        user = game.player_2
    game.choose_position(user)
    if game.check_for_win():
        game.get_winner()
        break
    current_round += 1
