import random
import json
import os

class Balance:
    def __init__(self):
        self.file_path = "player_save.json"

        if not os.path.exists(self.file_path) or os.path.getsize(self.file_path) == 0:
            self.balance = 100
            self.save_balance()
        else:
            try:
                with open(self.file_path, "r") as f:
                    data = json.load(f)
                    self.balance = data.get("balance", 100)
            except:
                self.balance = 100
                self.save_balance()

    def fetch_balance(self):
        return self.balance

    def change_balance(self, new_balance):
        self.balance = new_balance
        self.save_balance()

    def save_balance(self):
        with open(self.file_path, "w") as f:
            json.dump({"balance": self.balance}, f, indent=4)


class mines_game():
    def __init__(self):
        self.bet = 0
        self.mines = 1
        self.grid_size = 25
        self.grid = []
        self.multiplier = 0
        self.game_state = "None" #None for start #Active for alive #Lost for loss #Won for win

    def change_value(self, value_name, new_value):
        if self.game_state == "None":
            match value_name:
                case "bet":
                    self.bet = new_value
                case "mines":
                    self.mines = new_value
                case "grid_size":
                    self.grid_size = new_value

    def generate_grid(self):
        if self.game_state == "None":
            self.grid.clear()

            for i in range(self.grid_size):
                self.grid.append("G")

            if self.mines >= self.grid_size:
                print("ERROR: self.mines must be smaller than total self.grid_size.")
                return

            for mine in range(self.mines):
                index = random.randint(0, self.grid_size - 1)
                while self.grid[index] == "M":
                    index = random.randint(0, self.grid_size - 1)
                self.grid[index] = "M"
    
    def print_cells(self):
        print(self.grid)

game = mines_game()

game.generate_grid()
game.print_cells()

