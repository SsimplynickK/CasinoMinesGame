# Modules
import random
import customtkinter as ctk
from PIL import Image

# Config

grid_multiplier = 5
grid_size = grid_multiplier**2
mines_amount = 1

# Main functionality

app = ctk.CTk()

grid = []

def generate_grid():

    for i in range(grid_size):
        grid.append("💎")

    for i in range(mines_amount):
        if mines_amount >= grid_size:
            print("ERROR: Mines amount must smaller than amount of squares.")
            break
        else:
            mine = random.randint(0,grid_size-1)
            if grid[mine] == "💣":
                while grid[mine] != "💎":
                    mine = random.randint(0,grid_size-1)
            grid[mine] = "💣"

def print_grid():

    result = f''
    for i in range(len(grid)):
        result += str(grid[i]) + ' '
        if (i + 1) % grid_multiplier == 0:
            result += '\n'
    print(result)

def ui_init():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("ctk_theme.json")

    theme = ctk.ThemeManager.theme["CTk"]["fg_color"]
    
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()

    screen_center_x = int((screen_width / 2) - (500 / 2))
    screen_center_y = int((screen_height / 2) - (500 / 2))
    
    app.configure(fg_color=theme)
    app.geometry(f'500x500+{screen_center_x}+{screen_center_y}')
    app.title("Casino Mines Game")
    app.attributes('-topmost', True)
    app.overrideredirect(True)

    app.update_idletasks()

    global manager 
    manager = ctk.CTkToplevel(app)
    manager.configure(fg_color=theme)
    manager.title("Manager")
    manager.geometry(f'250x500+{screen_center_x-250}+{screen_center_y}')
    manager.attributes('-topmost', True)
    manager.overrideredirect(True)

    global tracker 
    tracker = ctk.CTkToplevel(app)
    tracker.configure(fg_color=theme)
    tracker.title("Tracker")
    tracker.geometry(f'250x500+{screen_center_x+500}+{screen_center_y}')
    tracker.attributes('-topmost', True)
    tracker.overrideredirect(True)

    global topbar 
    topbar = ctk.CTkToplevel(app)
    topbar.configure(fg_color="#0F0D25")
    topbar.title("Topbar")
    topbar.geometry(f'1000x35+{screen_center_x-250}+{screen_center_y-60}')
    topbar.attributes('-topmost', True)
    topbar.overrideredirect(True)

    global bottom_padding_window 
    bottom_padding_window = ctk.CTkToplevel(app)
    bottom_padding_window.configure(fg_color=theme)
    bottom_padding_window.title("bottom_padding_window")
    bottom_padding_window.geometry(f'1000x25+{screen_center_x-250}+{screen_center_y-25}')
    bottom_padding_window.attributes('-topmost', True)
    bottom_padding_window.overrideredirect(True)

    global top_padding_window 
    top_padding_window = ctk.CTkToplevel(app)
    top_padding_window.configure(fg_color=theme)
    top_padding_window.title("top_padding_window")
    top_padding_window.geometry(f'1000x25+{screen_center_x-250}+{screen_center_y+500}')
    top_padding_window.attributes('-topmost', True)
    top_padding_window.overrideredirect(True)

def generate_ui_grid():
    current_column = 0
    current_row = 0
    for i in range(grid_size):
        button_size = (500 * 0.9) / grid_multiplier
        padding_size = (500 * 0.1) / (grid_multiplier + 1)

        if current_column == 0:
            padx = (padding_size, padding_size / 2)
        elif current_column == grid_multiplier - 1:
            padx = (padding_size / 2, padding_size)
        else:
            padx = (padding_size / 2, padding_size / 2)

        if current_row == 0:
            pady = (padding_size, padding_size / 2)
        elif current_row == grid_multiplier - 1:
            pady = (padding_size / 2, padding_size)
        else:
            pady = (padding_size / 2, padding_size / 2)

        button = ctk.CTkButton(app, width=button_size, height=button_size, text="")
        button.grid(row=current_row, column=current_column, padx=padx, pady=pady)

        if (current_column + 1) % grid_multiplier == 0:
            current_row += 1
            current_column = 0
        else:
            current_column += 1

def topbar_init():
    button = ctk.CTkButton(topbar, width=25, height=25, text="❌", command=app.destroy, fg_color="#6C3131", hover_color="#794F4F", corner_radius=0)
    button.pack(side="right", padx=5, pady=5)

    icon = ctk.CTkImage(dark_image=Image.open("bomb_emoji.png"),size=(25,25))
    icon_label = ctk.CTkLabel(topbar, width=25, height=25, image=icon, text="")
    icon_label.pack(side="left", padx=5, pady=5)

    title = ctk.CTkLabel(topbar, width=100, height=25, text="Casino Mines Game")
    title.pack(side="left", padx=0, pady=5)

def manager_init():
    input_frame = ctk.CTkFrame(manager, fg_color="transparent")
    input_frame.pack(padx=15, pady=15, fill="x")

    bet_label = ctk.CTkLabel(input_frame, text="Bet Amount", anchor="w")
    bet_label.pack(side="top", anchor="w")

    bet_input = ctk.CTkEntry(input_frame, placeholder_text="$0.00")
    bet_input.pack(side="top", fill="x", pady=(5,0))
 
    grid_frame = ctk.CTkFrame(manager, fg_color="transparent")
    grid_frame.pack(padx=15, pady=15, fill="x")

    grid_label = ctk.CTkLabel(grid_frame, text="Grid Size", anchor="w")
    grid_label.pack(side="top", anchor="w")

    grid_options = ["25", "36", "49", "64"]
    segmented_button = ctk.CTkSegmentedButton(
        grid_frame,
        values=grid_options,
        command=lambda value: print("Selected Grid Size:", value)
    )
    segmented_button.set("25")
    segmented_button.pack(side="top", fill="x", pady=(5,0))

# Run

generate_grid()
print_grid()
ui_init()
generate_ui_grid()
topbar_init()
manager_init()
app.mainloop()