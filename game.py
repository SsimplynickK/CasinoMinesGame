import random
import json

class balance():
    def __init__(self):
        self.balance_save = open("player_save.json")

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

